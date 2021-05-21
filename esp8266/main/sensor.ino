
void changeMux(int c, int b, int a) {
  digitalWrite(MUX_A, a);
  digitalWrite(MUX_B, b);
  digitalWrite(MUX_C, c);
}

void sensorValue(int *light, int *dry, int* ph) {
  changeMux(LOW, LOW, LOW);
  *light = analogRead(ANALOG_INPUT); //Value of the sensor connected Option 0 pin of Mux
  delay(10);

  changeMux(LOW, LOW, HIGH);
  *dry = analogRead(ANALOG_INPUT); //Value of the sensor connected Option 0 pin of Mux
  delay(10);

  changeMux(LOW, HIGH, LOW);
  *ph = analogRead(ANALOG_INPUT); //Value of the sensor connected Option 0 pin of Mux
  delay(10);
}

void sendSensorData()
{
    DynamicJsonDocument doc(1024);
    int Ph = 0;
    int Light = 0;
    int Mositure = 0;

    sensorValue(&Light, &Mositure, &Ph);
    
    doc["Ph"] = Ph;
    doc["Light"] = Light; 
    doc["Mositure"] = Mositure;
    char jsonChar[100];
    serializeJson(doc, jsonChar);   
    client.publish(mqttTopics, jsonChar);
}
