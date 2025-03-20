from hardware_interface.ultrasonic import Rangefinder
import time

rf = Rangefinder()
while True:
    rf.print_range()



# def main():
#     test()

# if __name__ == "__main__":
#     main()