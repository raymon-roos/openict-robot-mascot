# '''

# This is example code for controlling the esp32 connected to the motor driver

# '''
# import time
# import serial
# import pyautogui

# screen_size_x, screen_size_y = pyautogui.size()

# ser = serial.Serial()

# ser.baudrate = 115200
# ser.port = "COM4"

# # The arguments for this function MUST be between (and including) 0-254, but may not be higher than 255
# def sendMotorCommand(directionA: int, speedA: int, directionB: int, speedB: int):
#     if 0 > directionA > 1 or 0 > speedA > 254 or 0 > directionB > 1 or 0 > speedB > 254:
#         print("motor command is not in a valid range 0-254 for speeds or 0-1 for directions")
#         return

#     ser.flush()
#     ser.write(bytes([directionA, speedA, directionB, speedB]))

# def sendSpeedFromMousePosition():
#     mouse_x, mouse_y = pyautogui.position()

#     speed_a = int((mouse_x / screen_size_x) * 254)
#     speed_b = int((mouse_y / screen_size_y) * 254)

#     ser.write(bytes([0, speed_a, 0, speed_b]))
#     ser.flush()

# def main():
#     ser.open()
#     ser.flush()
#     ser.write(bytes([0, 0, 0, 0]))
#     time.sleep(5)

#     # while True:
#     #     # sendSpeedFromMousePosition()
#     #     ser.write(bytes([0, 255, 0, 255]))
#     #     time.sleep(1)
#     for i in range(4):
#         ser.write(bytes([0, 255, 0, 255]))
#         time.sleep(1)
#         ser.write(bytes([0, 0, 0, 255]))
#         time.sleep(1)
        

#     ser.close()

# if __name__ == "__main__":
#     main()




import serial

class MotorController:
    serial = None

    def __init__(self):
        self.serial = serial.Serial('/dev/ttyUSB')