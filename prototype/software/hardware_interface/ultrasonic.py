# Importing Libraries 
import serial 
import time



class Rangefinder:
      def __init__(self, port='COM4'):
            self.arduino = serial.Serial(port, baudrate=115200, timeout=1) #'/dev/ttyACM0' ubuntu | 'COM4' windows
            self.arduino.read_all()

      def read(self):
            # request data
            self.arduino.write(b"0")
            data = self.arduino.readline()
            data = data.decode('utf-8').split(",")

            # return an array of 3 floating point values
            if data.__len__() != 3:
                  # check if data is received correctly
                  return (float(0), float(0), float(0))
            else:
                  return (float(data[0]), float(data[1]), float(data[2]))

      def print_range(self): 
            value = self.read()
            if len(value) != 0:
                  print(value)