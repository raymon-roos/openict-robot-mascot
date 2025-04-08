from hardware_interface.ultrasonic import Rangefinder
import time

# making an instance of the class
rf = Rangefinder()

while True:
    rf.print_range() # calling the function
    time.sleep(0.05)



