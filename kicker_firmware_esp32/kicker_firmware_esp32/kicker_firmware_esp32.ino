#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "sunrise_TIGO";  // Horizon X3 Pi hotspot SSID
const char* password = "";  // Horizon X3 Pi hotspot password
int connexionDuration;
WebServer server(80);

void handleInterrupt() {
  Serial.println("#########");
  Serial.println("DAKA");
  Serial.println("#########");
  digitalWrite(2,HIGH);
  delay(500);
  digitalWrite(2,LOW);           // Wait for 1 second before repeating
  delay(500);
  digitalWrite(2,HIGH);
  delay(500);
  digitalWrite(2,LOW);           // Wait for 1 second before repeating
  delay(500);
}

void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  connexionDuration = 0;
  // Connect to Horizon X3 Pi hotspot
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
    connexionDuration = connexionDuration + 1;
  }
  Serial.print("Connected to Horizon X3 Pi hotspot after ");
  Serial.print(connexionDuration);
  Serial.println("s");

  Serial.print("ESP32 IP address: ");
  Serial.println(WiFi.localIP());

  // Define HTTP endpoint
  server.on("/trigger", HTTP_GET, []() {
    handleInterrupt();
    server.send(200, "text/plain", "Interrupt triggered");
  });

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
