# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lib/qt/cnctoolbox/mainwindow.ui'
#
# Created: Sun Apr  5 14:35:20 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 636)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label_heading = QtWidgets.QLabel(self.centralWidget)
        self.label_heading.setGeometry(QtCore.QRect(340, 0, 211, 41))
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Pagella")
        font.setPointSize(36)
        font.setItalic(True)
        self.label_heading.setFont(font)
        self.label_heading.setObjectName("label_heading")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(190, 160, 701, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_opengl = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_opengl.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grid_opengl.setContentsMargins(0, 0, 0, 0)
        self.grid_opengl.setObjectName("grid_opengl")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 160, 171, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_xyz = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_xyz.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_xyz.setObjectName("verticalLayout_xyz")
        self.lcdNumber_mx = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdNumber_mx.setDigitCount(8)
        self.lcdNumber_mx.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_mx.setProperty("value", 8888.888)
        self.lcdNumber_mx.setObjectName("lcdNumber_mx")
        self.verticalLayout_xyz.addWidget(self.lcdNumber_mx)
        self.lcdNumber_my = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdNumber_my.setDigitCount(8)
        self.lcdNumber_my.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_my.setProperty("value", 8888.888)
        self.lcdNumber_my.setObjectName("lcdNumber_my")
        self.verticalLayout_xyz.addWidget(self.lcdNumber_my)
        self.lcdNumber_mz = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdNumber_mz.setSmallDecimalPoint(False)
        self.lcdNumber_mz.setDigitCount(8)
        self.lcdNumber_mz.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_mz.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_mz.setProperty("value", 8888.888)
        self.lcdNumber_mz.setObjectName("lcdNumber_mz")
        self.verticalLayout_xyz.addWidget(self.lcdNumber_mz)
        self.pushButton_connect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_connect.setGeometry(QtCore.QRect(10, 60, 95, 31))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_disconnect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_disconnect.setGeometry(QtCore.QRect(120, 60, 95, 31))
        self.pushButton_disconnect.setObjectName("pushButton_disconnect")
        self.pushButton_homing = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_homing.setGeometry(QtCore.QRect(230, 60, 95, 31))
        self.pushButton_homing.setObjectName("pushButton_homing")
        self.pushButton_killalarm = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_killalarm.setGeometry(QtCore.QRect(340, 60, 95, 31))
        self.pushButton_killalarm.setObjectName("pushButton_killalarm")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(450, 60, 95, 31))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_hold = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_hold.setGeometry(QtCore.QRect(10, 300, 71, 31))
        self.pushButton_hold.setObjectName("pushButton_hold")
        self.pushButton_resume = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_resume.setGeometry(QtCore.QRect(10, 340, 71, 31))
        self.pushButton_resume.setObjectName("pushButton_resume")
        self.pushButton_abort = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_abort.setGeometry(QtCore.QRect(10, 380, 71, 31))
        self.pushButton_abort.setObjectName("pushButton_abort")
        self.label_grbl = QtWidgets.QLabel(self.centralWidget)
        self.label_grbl.setGeometry(QtCore.QRect(240, 540, 361, 21))
        self.label_grbl.setText("")
        self.label_grbl.setObjectName("label_grbl")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(787, 30, 101, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_fileload = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_fileload.setGeometry(QtCore.QRect(690, 60, 95, 31))
        self.pushButton_fileload.setObjectName("pushButton_fileload")
        self.label_file = QtWidgets.QLabel(self.centralWidget)
        self.label_file.setGeometry(QtCore.QRect(390, 90, 501, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_file.setFont(font)
        self.label_file.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_file.setObjectName("label_file")
        self.pushButton_filestream = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_filestream.setGeometry(QtCore.QRect(790, 60, 95, 31))
        self.pushButton_filestream.setObjectName("pushButton_filestream")
        self.label_state = QtWidgets.QLabel(self.centralWidget)
        self.label_state.setGeometry(QtCore.QRect(10, 120, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_state.setFont(font)
        self.label_state.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_state.setObjectName("label_state")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 420, 171, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber_wx = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_wx.setDigitCount(8)
        self.lcdNumber_wx.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_wx.setProperty("value", 8888.888)
        self.lcdNumber_wx.setObjectName("lcdNumber_wx")
        self.verticalLayout.addWidget(self.lcdNumber_wx)
        self.lcdNumber_wy = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_wy.setDigitCount(8)
        self.lcdNumber_wy.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_wy.setProperty("value", 8888.888)
        self.lcdNumber_wy.setObjectName("lcdNumber_wy")
        self.verticalLayout.addWidget(self.lcdNumber_wy)
        self.lcdNumber_wz = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_wz.setDigitCount(8)
        self.lcdNumber_wz.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_wz.setProperty("value", 8888.888)
        self.lcdNumber_wz.setObjectName("lcdNumber_wz")
        self.verticalLayout.addWidget(self.lcdNumber_wz)
        self.pushButton_zeroxyz = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_zeroxyz.setGeometry(QtCore.QRect(110, 300, 71, 31))
        self.pushButton_zeroxyz.setObjectName("pushButton_zeroxyz")
        self.pushButton_zeroz = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_zeroz.setGeometry(QtCore.QRect(110, 380, 71, 31))
        self.pushButton_zeroz.setObjectName("pushButton_zeroz")
        self.pushButton_zeroxy = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_zeroxy.setGeometry(QtCore.QRect(110, 340, 71, 31))
        self.pushButton_zeroxy.setObjectName("pushButton_zeroxy")
        self.label_currentgcodeblock = QtWidgets.QLabel(self.centralWidget)
        self.label_currentgcodeblock.setGeometry(QtCore.QRect(660, 120, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_currentgcodeblock.setFont(font)
        self.label_currentgcodeblock.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_currentgcodeblock.setObjectName("label_currentgcodeblock")
        self.pushButton_g0wzero = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_g0wzero.setGeometry(QtCore.QRect(800, 560, 91, 31))
        self.pushButton_g0wzero.setObjectName("pushButton_g0wzero")
        self.pushButton_g0wzerosafe = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_g0wzerosafe.setGeometry(QtCore.QRect(640, 560, 151, 31))
        self.pushButton_g0wzerosafe.setObjectName("pushButton_g0wzerosafe")
        self.pushButton_w2mcoord = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_w2mcoord.setGeometry(QtCore.QRect(190, 560, 111, 31))
        self.pushButton_w2mcoord.setObjectName("pushButton_w2mcoord")
        self.lineEdit_cmdline = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_cmdline.setGeometry(QtCore.QRect(190, 120, 301, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_cmdline.setFont(font)
        self.lineEdit_cmdline.setObjectName("lineEdit_cmdline")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "cnctoolbox"))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.pushButton_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.pushButton_homing.setText(_translate("MainWindow", "Homing"))
        self.pushButton_killalarm.setText(_translate("MainWindow", "Kill Alarm"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_hold.setText(_translate("MainWindow", "Hold"))
        self.pushButton_resume.setText(_translate("MainWindow", "Resume"))
        self.pushButton_abort.setText(_translate("MainWindow", "Abort"))
        self.pushButton_fileload.setText(_translate("MainWindow", "Load File"))
        self.label_file.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_filestream.setText(_translate("MainWindow", "Stream File"))
        self.label_state.setText(_translate("MainWindow", "disconnected"))
        self.pushButton_zeroxyz.setText(_translate("MainWindow", "Zero XYZ"))
        self.pushButton_zeroz.setText(_translate("MainWindow", "Zero Z"))
        self.pushButton_zeroxy.setText(_translate("MainWindow", "Zero XY"))
        self.label_currentgcodeblock.setText(_translate("MainWindow", "---"))
        self.pushButton_g0wzero.setText(_translate("MainWindow", "G0 WZero"))
        self.pushButton_g0wzerosafe.setText(_translate("MainWindow", "G0 WZero (safe)"))
        self.pushButton_w2mcoord.setText(_translate("MainWindow", "W -> M Coord"))

