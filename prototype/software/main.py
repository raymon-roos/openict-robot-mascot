# from hardware_interface.ultrasonic import Rangefinder
from hardware_interface.motorcontrol import MotorController
import time

def main():
    motorcontroller = MotorController()

    motorcontroller.drive(MotorController.RIGHT, 100, MotorController.LEFT, 100)
    time.sleep(1)
    motorcontroller.stop()
    time.sleep(1)
    motorcontroller.drive(MotorController.RIGHT, 254, MotorController.LEFT, 254)
    time.sleep(1)
    motorcontroller.stop()



if __name__ == "__main__":
    main()