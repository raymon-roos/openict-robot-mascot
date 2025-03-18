# Serial control protocol

This code is used to control a motor controller which in turn controls a small car with 2 dc motors.
There's some *very raw* logic to control the motors over serial from a parent device (in our case, a raspberry pi)

This is how it works:

The esp32 listens over serial for 4 bytes. These 4 bytes are laid out like this:

```C
[motor direction 1, motor speed 1, motor direction 2, motor speed 2]
```

Where the motor directions are a byte that should either be 0 or 1 for left/right (where left/right is highly dependant on how I connected the wires on the controller and thus not very standardized lol), and the motor speed is the full size of the byte ranging from 0-254

In the python script provided in my parent directory sits a small example which translates mouse coordinates to speeds on the motor and sends it.