import json
from src.jsonUtils import jsonUtils

class monitor:
    mqtt_cmd_rec_count = 0
    node_online_status_executed = False
    node_sensor_data_get_status_executed = False
    node_online_status_payload = ""
    node_sensor_data_payload = ""
    mqtt_data_received = False
    client = None
    topic = "home/node1"

    def __init__(self):
        pass

    def publish_node_status_get(self, client):
        client.publish(self.topic, 'NODE_ONLINE_STATUS_GET')
        self.node_online_status_executed = True
        pass

    def publish_sensor_data_get(self, client):
        client.publish(self.topic, 'GET_SENSOR_DATA')
        self.node_sensor_data_get_status_executed = True
        pass

    def mqtt_on_msg_callback(self, payload):
        jsonData = {
            "light": 0,
            "dry": 0,
            "ph": 0,
            "relay_ctrl": "OFF",
            "node": "Device Not Connected"
        }

        if str(payload).find("cmd") > -1:
            if str(payload).find("NODE_ONLINE_STATUS_GET") > -1:
                self.node_online_status_payload = str(payload)
                self.node_online_status_executed = False

            if str(payload).find("GET_SENSOR_DATA") > -1:
                self.node_sensor_data_payload = str(payload)
                self.node_sensor_data_get_status_executed = False
                self.mqtt_data_received = True
                pass


        if not self.node_online_status_executed and not self.node_sensor_data_get_status_executed and self.mqtt_data_received:
            device_connected_status = False

            if self.node_online_status_payload: 
                if (self.node_online_status_payload).find("I am alive") > -1:
                    device_connected_status = True
            
            if self.node_sensor_data_payload:
     
                sensor_data = json.loads(self.node_sensor_data_payload)
                jsonData['ph'] = sensor_data['Ph']
                jsonData['dry'] = sensor_data['Moisture']
                jsonData['light'] = sensor_data['Light']

                if self.relaySystemMonitor(sensor_data): 
                    jsonData['relay_ctrl'] = "ON"
                else:
                    jsonData['relay_ctrl'] = "OFF"

                if device_connected_status: 
                    jsonData['node'] = "Device Connected"
                else:
                    print(self.node_online_status_payload)
                    jsonData['node'] = "Device Not Connected"

                jsonUtils().construct_data(jsonData)

            self.mqtt_data_received = False
            self.node_sensor_data_payload = ""
            self.node_online_status_payload = ""
            pass

    def relaySystemMonitor(self, sensor_data):
        print(sensor_data)
        if(sensor_data['Moisture'] < 100):
            return True
        
        return False

    def scheduler_task(self, client):
        self.publish_node_status_get(client)
        self.publish_sensor_data_get(client)
        pass
