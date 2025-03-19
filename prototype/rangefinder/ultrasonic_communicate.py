# Importing Libraries 
import serial 
import time 
arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1) #'/dev/ttyACM0' ubuntu | 'COM4' windows

class Rangefinder:
      # def __init__(self):# Constructor (init-methode) wordt automatisch aangeroepen bij het maken van een object
      def read(self):
            arduino.write(bytes('0', 'utf-8'))  
            data = arduino.readline().decode('utf-8') # utf-8' voor windows
            return data 

      def print_range(self): 
            value = self.read()
            if len(value) != 0:
                  print(value) 
                  




