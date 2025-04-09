# Importing Libraries 
import serial 
import time



class Rangefinder:
      def __init__(self, port='COM4'):
            self.arduino = serial.Serial(port, baudrate=115200, timeout=.1) #'/dev/ttyACM0' ubuntu | 'COM4' windows

      def read(self):
            self.arduino.write(bytes('0', 'utf-8'))  
            data = self.arduino.readline().decode('utf-8') # utf-8' voor windows
            return data 

      def print_range(self): 
            value = self.read()
            if len(value) != 0:
                  print(value)