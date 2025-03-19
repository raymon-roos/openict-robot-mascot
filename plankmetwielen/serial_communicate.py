# Importing Libraries 
import serial 
import time 
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1) #'/dev/ttyACM0' ubuntu | 'COM4' windows

def write_read(x): 
	arduino.write(bytes(x, 'iso-8859-1')) #'iso-8859-1' voor ubuntu
	time.sleep(0.05) 
	data = arduino.readline().decode('iso-8859-1') # utf-8' voor windows
	return data 



while True: 
    num = '0'
    value = write_read(num)
    value = value.split(",")
    print(value) 
    time.sleep(0.1)
    # if value != 0:
    #      output = value
    #      output = int(output)
    #     #  formatted_number = "%.2f" % output
    #      print(output)
    # else:
    #     output = 0
        
