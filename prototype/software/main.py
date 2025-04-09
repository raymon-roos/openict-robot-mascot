from hardware_interface.ultrasonic import Rangefinder
from hardware_interface.motorcontrol import MotorController
import time
import serial.tools.list_ports;

# https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python

def drive_motor():
    motorcontroller = MotorController()

    motorcontroller.drive(MotorController.RIGHT, 100, MotorController.LEFT, 100)
    time.sleep(1)
    motorcontroller.stop()
    time.sleep(1)
    motorcontroller.drive(MotorController.RIGHT, 254, MotorController.LEFT, 254)
    time.sleep(1)
    motorcontroller.stop()

def read_ultrasonic():
    reader = Rangefinder()

    while True:
        dst_str = reader.read()

        if dst_str.__len__() == 0: continue

        # print 3 floats
        print()

        time.sleep(0.1)

def main():
    print([comport.device for comport in serial.tools.list_ports.comports()])

    # drive_motor
    read_ultrasonic()

if __name__ == "__main__":
    main()