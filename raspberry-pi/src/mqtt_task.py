from apscheduler.events import SchedulerEvent
import paho.mqtt.client as mqtt
from src.monitor import monitor

class mqtt_task:
    topic = "home/node1"
    hostAddress = '192.168.0.136'
    client = mqtt.Client()
    monitor_obj = monitor()
    
    def __init__(self):
        pass
    
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        # Check if this is a message for the Pi LED.
        print(msg.payload)
        if msg.topic == self.topic:
            if str(msg.payload).find("cmd") > -1:
                print(msg.payload)
                self.monitor_obj.mqtt_on_msg_callback(str(msg.payload, 'utf-8'))

    def scheduler_task(self):
        self.monitor_obj.scheduler_task(self.client)

    def setup(self):
        # Create MQTT client and connect to localhost, i.e. the Raspberry Pi running
        # this script and the MQTT server.
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.hostAddress, 1883, 60)
        # Connect to the MQTT server and process messages in a background thread.
        self.client.loop_start()
        
        pass