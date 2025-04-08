#include <Arduino.h>
#include <WebServer.h>
#include <WiFi.h>

// Wi-Fi credentials
const char *ssid = "ESP32-Car";
const char *password = "12345678";

WebServer server(80);

#define RELAY_INPUT_PIN 33

void handleRoot();
void handleCommand();
void emergencyStop();
void restart();

void setup() {
  pinMode(RELAY_INPUT_PIN, OUTPUT);
  digitalWrite(RELAY_INPUT_PIN, HIGH);

  Serial.begin(115200);

  // Start Wi-Fi Access Point
  WiFi.softAP(ssid, password);
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());

  // Define API routes
  server.on("/", handleCommand);

  server.begin();
  Serial.println("Web server started");
}

void loop() { server.handleClient(); }

// Serve the control page
void sendFormResponse() {
  server.send(200, "text/html", R"EOF(
<!DOCTYPE html>
<html>
<head>
    <title>ESP32 Control</title>
</head>
<body>
    <h1>ESP32 Car Control</h1>
    <p>Send commands over HTTP: 192.168.4.1/do?command=[command]</p>
    <p>Where [command] is one of:</p>
    <ul>
        <li>estop</li>
        <li>restart</li>
    </ul>
    <a href="?command=estop"><button>EMERGENCY STOP</button></a>
    <br><br>
    <a href="?command=restart"><button>restart</button></a>
</body>
</html>
)EOF");
}

// Process movement commands
void handleCommand() {
  if (server.hasArg("command")) {
    String command = server.arg("command");
    Serial.println("command: " + command);

    if (command == "estop")
      emergencyStop();
    else if (command == "restart")
      restart();
    else {
      server.send(400, "text/plain", "Incorrect `command` parameter");
      return;
    }
  }

  sendFormResponse();
}

void emergencyStop() { digitalWrite(RELAY_INPUT_PIN, LOW); }

void restart() { digitalWrite(RELAY_INPUT_PIN, HIGH); }
