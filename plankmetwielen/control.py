import time
import serial
import pyautogui

screen_size_x, screen_size_y = pyautogui.size()

ser = serial.Serial()

ser.baudrate = 115200
ser.port = "COM4"

def sendSpeedFromMousePosition():
    mouse_x, mouse_y = pyautogui.position()

    speed_a = int((mouse_x / screen_size_x) * 254)
    speed_b = int((mouse_y / screen_size_y) * 254)

    ser.write(bytes([0, speed_a, 0, speed_b]))
    ser.flush()

def main():
    ser.open()
    ser.flush()
    ser.write(bytes([0, 0, 0, 0]))
    time.sleep(5)

    # while True:
    #     # sendSpeedFromMousePosition()
    #     ser.write(bytes([0, 255, 0, 255]))
    #     time.sleep(1)
    for i in range(4):
        ser.write(bytes([0, 255, 0, 255]))
        time.sleep(1)
        ser.write(bytes([0, 0, 0, 255]))
        time.sleep(1)
        

    ser.close()

if __name__ == "__main__":
    main()