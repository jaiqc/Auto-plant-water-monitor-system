
#define MUX_A D3
#define MUX_B D4
#define MUX_C D5

#define ANALOG_INPUT A0
#define RELAY_CTRL_SYSTEM D8

// MQTT Configuration
#define WIFI_SSID     "Home_Ext"
#define WIFI_PASSWORD "9894102639"
#define MQTT_SERVER   "192.168.0.136" // IP adress Raspberry Pi
#define MQTT_PORT     1883
#define MQTT_USER     "home"
#define MQTT_PASSWORD "9894102639"
#define MQTT_TOPICS   "home/node1"

typedef enum NODE_OPERATION {
  NODE_IDLE,
  NODE_SEND_SENSOR_DATA,
  NODE_RELAY_SYSTEM_ON,
  NODE_RELAY_SYSTEM_OFF
};

#define GET_SENSOR_DATA "GET_SENSOR_DATA"
#define RELAY_SYSTEM_ON "RELAY_SYSTEM_ON"
#define RELAY_SYSTEM_OFF "RELAY_SYSTEM_OFF"
