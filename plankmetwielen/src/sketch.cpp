#include <Arduino.h>

#define BAUD_RATE 115200

#define MA_PIN_IN2 15
#define MA_PIN_IN1 16
#define MA_PIN_ENABLE 17

#define MB_PIN_IN1 22
#define MB_PIN_IN2 23
#define MB_PIN_ENABLE 21

typedef struct Motor {
    int pin_in1, pin_in2;
    int pin_enable;
} Motor;

typedef enum MotorDirection {
    LEFT = 0,
    RIGHT
} MotorDirection;

void motor_init(Motor &m);
void motor_drive(Motor &m, MotorDirection dir, uint8_t speed);

static Motor motor_a = { .pin_in1 = MA_PIN_IN1, .pin_in2 = MA_PIN_IN2, .pin_enable = MA_PIN_ENABLE };
static Motor motor_b = { .pin_in1 = MB_PIN_IN1, .pin_in2 = MB_PIN_IN2, .pin_enable = MB_PIN_ENABLE };

void setup()
{
    Serial.begin(BAUD_RATE);

    motor_init(motor_a);
    motor_init(motor_b);

    // temp
    motor_drive(motor_a, LEFT, 100);
    motor_drive(motor_b, LEFT, 100);
}

void loop()
{
    if (Serial.available() >= 4) {
        
        char buffer[4];

        Serial.readBytes(buffer, 4);

        uint8_t 
            motorSpeed_a = (uint8_t)buffer[1],
            motorSpeed_b = (uint8_t)buffer[3];
        MotorDirection
            motorDirection_a = (MotorDirection)buffer[0],
            motorDirection_b = (MotorDirection)buffer[2];

        motor_drive(motor_a, motorDirection_a, motorSpeed_a);
        motor_drive(motor_b, motorDirection_b, motorSpeed_b);
    }
}

void motor_init(Motor &m)
{
    pinMode(m.pin_in1, OUTPUT);
    pinMode(m.pin_in2, OUTPUT);
    pinMode(m.pin_enable, OUTPUT);
}

void motor_drive(Motor &m, MotorDirection dir, uint8_t speed)
{
    uint8_t va = HIGH, vb = LOW;

    if (dir == LEFT) { va = LOW; vb = HIGH; }

    // direction
    digitalWrite(m.pin_in1, va);
    digitalWrite(m.pin_in2, vb);

    analogWrite(m.pin_enable, speed);
}