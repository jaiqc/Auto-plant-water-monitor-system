#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include "config.h"

// https://www.youtube.com/watch?v=axhakHVXM9U
// https://github.com/EnhaoSun/ESP8266-MQTT-RaspberryPi

const char* ssid = WIFI_SSID;                   // wifi ssid
const char* password =  WIFI_PASSWORD;         // wifi password
const char* mqttServer = MQTT_SERVER;    // IP adress Raspberry Pi
const int mqttPort = MQTT_PORT;
const char* mqttUser = MQTT_USER;      // if you don't have MQTT Username, no need input
const char* mqttPassword = MQTT_PASSWORD;  // if you don't have MQTT Password, no need input
const char* mqttTopics = MQTT_TOPICS;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  pinMode(MUX_A, OUTPUT);
  pinMode(MUX_B, OUTPUT);     
  pinMode(MUX_C, OUTPUT);  

  pinMode(RELAY_CTRL_SYSTEM, OUTPUT);  
  
  Serial.begin(115200);
  
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  
  Serial.println("Connected to the WiFi network");

  mqttBegin();
}

void loop() {
    client.subscribe(mqttTopics);
    client.loop();
}
