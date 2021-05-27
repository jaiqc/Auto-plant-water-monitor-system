
void mqttState(byte* payload, unsigned int length)
{
  char myData[256] = {0};

  for (int i = 0; i < length; i++) {
    myData[i] = (char)payload[i];
  }

  if(strncmp((char *)myData, GET_SENSOR_DATA, strlen(GET_SENSOR_DATA)) == 0) {
    nodeState(NODE_SEND_SENSOR_DATA);
  }
  
  if(strncmp((char *)myData, RELAY_SYSTEM_ON, strlen(RELAY_SYSTEM_ON)) == 0) {
    nodeState(NODE_RELAY_SYSTEM_ON);
  }

  if(strncmp((char *)myData, RELAY_SYSTEM_OFF, strlen(RELAY_SYSTEM_OFF)) == 0) {
    nodeState(NODE_RELAY_SYSTEM_OFF);
  }

  if(strncmp((char *)myData, NODE_ONLINE_STATUS_GET, strlen(NODE_ONLINE_STATUS_GET)) == 0) {
    nodeState(NODE_ONLINE_STATUS);
  }
}

void nodeState(NODE_OPERATION state)
{
  switch(state)
  {
    case NODE_IDLE:
      break;

    case NODE_ONLINE_STATUS:
      client.publish(mqttTopics, "I am alive");
      break;

    case NODE_SEND_SENSOR_DATA:
      Serial.println("sendSensorData");
      sendSensorData();
      break;

    case NODE_RELAY_SYSTEM_ON:
      Serial.println("relayCtrlSystemOn");
      relayCtrlSystemOn();
      break;

    case NODE_RELAY_SYSTEM_OFF:
      Serial.println("relayCtrlSystemOff");
      relayCtrlSystemOff();
      break;
  }
}
