
void mqttBegin()
{
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
   
    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
      Serial.println("connected");
    } else {
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
    }
  }

  client.publish(mqttTopics, mqttTopics);
  client.subscribe(mqttTopics);
}

void callback(char* topic, byte* payload, unsigned int length) {
  mqttState(payload, length);  
}
