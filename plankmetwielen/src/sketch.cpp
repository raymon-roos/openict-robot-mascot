#include <Arduino.h>

#define BAUD_RATE 115200

#define MA_PIN_IN2 15
#define MA_PIN_IN1 16
#define MA_PIN_ENABLE 17

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
static Motor motor_b = {}; // TODO

static uint8_t currentMotorSpeedA = 0;
static uint8_t currentMotorSpeedB = 0;

void setup()
{
    Serial.begin(BAUD_RATE);
}

void loop()
{

}

void motor_init(Motor m)
{
    pinMode(m.pin_in1, OUTPUT);
    pinMode(m.pin_in2, OUTPUT);
    pinMode(m.pin_enable, OUTPUT);
}

void motor_drive(Motor &m, MotorDirection dir, uint8_t speed)
{

}