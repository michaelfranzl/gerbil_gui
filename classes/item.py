import logging
import numpy as np
import ctypes
import sys
import math
import re

from PyQt5.QtCore import pyqtSignal, QPoint, Qt, QSize, QTimer
from PyQt5.QtGui import QColor, QMatrix4x4, QVector2D, QVector3D, QQuaternion
from PyQt5.QtOpenGL import QGLWidget

import OpenGL
OpenGL.ERROR_CHECKING = False
OpenGL.FULL_LOGGING = False
from OpenGL.GL import *

class Item():
    def __init__(self, prog, pt=GL_LINES, lw=1):
        self.vbo = glGenBuffers(1)
        self.vao = glGenVertexArrays(1)
        self.program = prog

        self.elementcount = 0
        
        self.matrix_model = QMatrix4x4()
        
        self.primitive_type = pt
        self.linewidth = lw
        
        self.data = np.zeros(10000000, [("position", np.float32, 3), ("color", np.float32, 4)])
        
        
    def append(self, pos, col=(1, 1, 1, 1)):
        self.data["position"][self.elementcount] = pos
        self.data["color"][self.elementcount] = col
        self.elementcount += 1
        
        
    def upload(self):
        # chop unneeded bytes
        self.data = self.data[0:self.elementcount]
        
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.data.nbytes, self.data, GL_DYNAMIC_DRAW)
        
        print("UPLOADING {} BYTES".format(self.data.nbytes))
        stride = self.data.strides[0]
        
        offset = ctypes.c_void_p(0)
        loc = glGetAttribLocation(self.program, "position")
        glEnableVertexAttribArray(loc)
        glVertexAttribPointer(loc, 3, GL_FLOAT, False, stride, offset)

        offset = ctypes.c_void_p(self.data.dtype["position"].itemsize)
        loc = glGetAttribLocation(self.program, "color")
        glEnableVertexAttribArray(loc)
        glVertexAttribPointer(loc, 4, GL_FLOAT, False, stride, offset)
        
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)
        
    def scale(self, fac):
        self.matrix_model.scale(fac)
        
    def translate(self, vec):
        self.matrix_model.translate(vec[0], vec[1], vec[2])
        
    def rotate(self, angle, vec):
        self.matrix_mode.rotate(angle, vec[0], vec[1], vec[2])
        
    def moveto(self, tpl):
        self.matrix_model.setToIdentity()
        self.translate(tpl)
        
    def draw(self):
        mat_m = self.qt_mat_to_array(self.matrix_model)
        loc_mat_m = glGetUniformLocation(self.program, "mat_m")
        glUniformMatrix4fv(loc_mat_m, 1, GL_TRUE, mat_m)
        
        # bind VBO and VAO
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        
        # actual draw command
        glLineWidth(self.linewidth)
        glDrawArrays(self.primitive_type, 0, self.elementcount)
        
        # unbind VBO and VAO
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)
    
    @staticmethod
    def qt_mat_to_array(mat):
        arr = [0] * 16
        for i in range(4):
            for j in range(4):
                idx = 4 * i + j
                arr[idx] = mat[i, j]
        return arr
        
        
        
class CoordSystem(Item):
    def __init__(self,
                 prog,
                 scale=1,
                 trans=(0, 0, 0)
                 ):
        
        super(CoordSystem, self).__init__(prog)
        
        self.primitive_type = GL_LINES
        self.linewidth = 3
        self.scale(scale)
        self.translate(trans)
        
        self.append((0, 0, 0), (1, 0, 0, 1))
        self.append((10, 0, 0), (1, 0, 0, 1))
        self.append((0, 0, 0), (0, 1, 0, 1))
        self.append((0, 10, 0), (0, 1, 0, 1))
        self.append((0, 0, 0), (0, 0, 1, 1))
        self.append((0, 0, 10), (0, 0, 1, 1))
        self.upload()
        

class Grid(Item):
    def __init__(self,
                 prog,
                 ll=(0, 0),
                 ur=(1000, 1000),
                 trans=(0, 0, 0),
                 unit=10
                 ):
        
        super(Grid, self).__init__(prog)
        
        self.primitive_type = GL_LINES
        self.linewidth = 1
        self.color = (0.5, 0.5, 0.5, 0.5)
        self.translate(trans)
        
        width = ur[0] - ll[0]
        height = ur[1] - ll[1]
        width_units = int(width / unit) + 1
        height_units = int(height / unit) + 1
        
        for wu in range(0, width_units):
            x = unit * wu
            self.append((x, 0, 0), self.color)
            self.append((x, height, 0), self.color)
            
        for hu in range(0, height_units):
            y = unit * hu
            self.append((0, y, 0), self.color)
            self.append((width, y, 0), self.color)

        self.upload()
        
        
class GcodePath(Item):
    def __init__(self, prog, gcode, cwpos, ccs, cs_offsets):
        
        super(GcodePath, self).__init__(prog)
        
        self.primitive_type = GL_LINE_STRIP
        self.linewidth = 1
        
        pos = list(cwpos) # current position
        cs = ccs # current coordinate system
        offset = cs_offsets[cs] # current offset tuple
        motion = "" # current motion mode
        
        colg0 = (1, 1, 1, 1)
        colg1 = (0.5, 0.5, 1, 1)

        axes = ["X", "Y", "Z"]
        contains_regexps = []
        for i in range(0, 3):
            axis = axes[i]
            contains_regexps.append(re.compile(".*" + axis + "([-.\d]+)"))
        
        # start of line
        target = np.add(offset, pos)
        self.append(tuple(target), colg0)
        
        for line in gcode:
            mm = re.match("G(\d).*", line)
            if mm: motion = "G" + mm.group(1)
            col = colg0 if motion == "G0" else colg1
                
            mcs = re.match("G(5[4-9]).*", line)
            if mcs: 
                cs = "G" + mcs.group(1)
                offset = cs_offsets[cs]
                
            for i in range(0, 3):
                axis = axes[i]
                cr = contains_regexps[i]
                
                m = re.match(cr, line)
                if m:
                    a = float(m.group(1))
                    pos[i] = a

            target = np.add(offset, pos)
            self.append(tuple(target), col)
        
        self.upload()
        
        
        
        