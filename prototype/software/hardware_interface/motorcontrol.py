import serial

class MotorController:
    serial = None

    LEFT = 0
    RIGHT = 1

    def __init__(self, port='/dev/ttyUSB0'):
        print("connecting to motor serial port")

        self.serial = serial.Serial(port)

    # on object destruction, close serial connection
    def __del__(self):
        print("closing serial connection")
        self.serial.close()

    def _isCorrectByteSize(self, val):
        if val < 0:
            raise ValueError(f"value {val} is out of range: less than 0")
        elif val > 254:
            raise ValueError(f"value {val} is out of range: higher than 254")
        else:
            return True

    def _sendBytes(self, a, b, c, d):
        if self._isCorrectByteSize(a) and self._isCorrectByteSize(b) and self._isCorrectByteSize(c) and self._isCorrectByteSize(d):
            self.serial.write(bytes([a, b, c, d]))

    def stop(self):
        self._sendBytes(0, 0, 0, 0)

    # drives both motors
    def drive(self, direction1, speed1, direction2, speed2):
        self._sendBytes(direction1, speed1, direction2, speed2)