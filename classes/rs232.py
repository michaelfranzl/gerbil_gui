import serial
import time
import multiprocessing
import signal
import logging

class RS232:
    def __init__(self, name="", path="/dev/null", baud=115200, callback=None):
        self.name = name
        self.path = path
        self.baud = baud
        self.cb = callback
        self.buf_receive = ""
        
    def start(self):
        logging.info("RS232 %s: connecting to %s", self.name, self.path)
        self.serialport = serial.Serial(self.path, self.baud, timeout=None)
        self.serialport.flushInput()
        self.serialport.flushOutput()
        time.sleep(1)
        self.serial_process = multiprocessing.Process(target=self.receiving)
        self.serial_process.start()
        print self.serial_process, self.serial_process.is_alive()
        
    def stop(self):
        self.cleanup()
        
        logging.info("RS232 %s: disconnecting from %s", self.name, self.path)
        self.serialport.close()
        self.serial_process.terminate()
        time.sleep(1)
        isalive = self.serial_process.is_alive()
        if isalive == False:
            logging.info("RS232 %s: has successfully terminated", self.serial_process)
        else:
            logging.info("WARNING! %s has not terminated within 1 second", self.serial_process)
        
    def cleanup(self):
        logging.info("RS232 %s: cleaning up before disconnecting", self.name)
        self.write("!\r\n") # feed hold
        logging.info("RS232 %s: ready to be disconnected", self.name)
        
    def write(self, data):
        if len(data) > 0:
            logging.info("RS232 %s:     -----------> %ibytes %s", self.name, len(data), data.strip())
            self.serialport.write(data)
        else:
            logging.info("RS232 %s: nothing to write", self.name)

    def receiving(self):
        while True:
            data = self.serialport.read(1)
            waiting = self.serialport.inWaiting()
            data += self.serialport.read(waiting)
            self.handle_data(data)
            
    def handle_data(self, data):
        for i in range(0, len(data)):
            self.buf_receive += data[i]
            if data[i] == "\n":
                self.cb(self.buf_receive.strip())
                self.buf_receive = ""
        