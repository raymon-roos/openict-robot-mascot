#include <Arduino.h>
#include <SRF05.h>

#define TRIG1 14
#define TRIG2 25
#define TRIG3 33

#define ECHO1 27 
#define ECHO2 26
#define ECHO3 32

// using the SRF05 library
SRF05
    range1(TRIG1, ECHO1),
    range2(TRIG2, ECHO2),
    range3(TRIG3, ECHO3);

void setup()
{
    Serial.begin(115200);
}

void loop()
{
    // don't send data if the master hasn't asked
    // for it by sending a single generic byte over serial
    if (!Serial.available()) return;
    // clear input buffer
    int c = Serial.read();

    // distance variables
    float d1, d2, d3;

    // prevent one sensor from reading the lingering audio wave
    // of another by waiting a bit before sending the next pulse
    d1 = range1.getMeter();
    delay(40);
    d2 = range2.getMeter();
    delay(40);
    d3 = range3.getMeter();
    delay(40);

    // output formatting
    Serial.print(d1); Serial.print(",");
    Serial.print(d2); Serial.print(",");
    Serial.print(d3); Serial.print("");
    Serial.println();
}