from hardware_interface.ultrasonic import Rangefinder
import time

rf = Rangefinder()
while True:
    rf.print_range()
    time.sleep(0.05)



# def main():
#     test()

# if __name__ == "__main__":
#     main()