int echoPin_1 = 3; // Echo van sensor 1 op pin 3
int trigPin_1 = 4;
int echoPin_2 = 5; // Echo van sensor 2 op pin 5
int trigPin_2 = 6;

int pingTime; // Variabele voor het meten van pingtijd
float speedOfSound = 0.0343; // Geluidssnelheid in cm/us
float afstand_voor = 0;
float afstand_achter = 0;

void setup() {
  pinMode(echoPin_1, INPUT);
  pinMode(trigPin_1, OUTPUT);
  pinMode(echoPin_2, INPUT);
  pinMode(trigPin_2, OUTPUT);
  
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  
  // Meet afstand voor
  digitalWrite(trigPin_1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin_1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin_1, LOW);

  pingTime = pulseIn(echoPin_1, HIGH);
  
  if (pingTime > 0) {  
    afstand_voor = (speedOfSound * pingTime) / 2.0; 

    // Meet afstand achter
    digitalWrite(trigPin_2, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin_2, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin_2, LOW);

    pingTime = pulseIn(echoPin_2, HIGH);

    if (pingTime > 0) {  
      afstand_achter = (speedOfSound * pingTime) / 2.0;
    } else {
      // Serial.print("Geen echo ontvangen!");
      afstand_achter = 0; // Zet op 0 als geen echo wordt ontvangen
    }

    // Stuur data naar de serial monitor
    Serial.print(afstand_voor, 0); // eerste waarde print 
    Serial.print(",");
    Serial.print(afstand_achter, 0); // tweede waarden in print
  }

  delay(100);
}
