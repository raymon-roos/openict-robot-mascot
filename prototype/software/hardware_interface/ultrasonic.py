# Importing Libraries 
import serial 



arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1) #'/dev/ttyACM0' ubuntu | 'COM4' windows

class Rangefinder:
      """making a class that gets and prints the data of a ultrasonic range sensor using serial communication"""

      def read(self):
            """function to get the value of the ultrasonic range sensors using serial communication"""
            arduino.write(bytes('0', 'utf-8'))  
            data = arduino.readline().decode('utf-8') # utf-8' voor windows | 'iso-8859-1' ubuntu
            return data 

      def print_range(self):
            """function that prints the value from the read function"""
            value = self.read()
            if len(value) != 0:
                  print(value)