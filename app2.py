
from flask import Flask, render_template, request
import time
import paho.mqtt.client as mqtt
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
client = mqtt.Client()

timeStamp = 0

def parse_func():
	timeStamp = time.time()
	return (timeStamp)


@app.route("/")
def index():
	timeStamp = parse_func()
	client.publish('home/node1', 'GET_SENSOR_DATA')
	templateData = {
      'button': timeStamp,
      'senPIR': timeStamp,
      'ledRed': timeStamp,
      'ledYlw': timeStamp,
      'ledGrn': timeStamp,
      }
	return render_template('index.html', **templateData)

# The function below is executed when someone requests a URL with the actuator name and action in it:


@app.route("/<deviceName>/<action>")
def action(deviceName, action):

	client.publish('home/node1', 'GET_SENSOR_DATA')
	timeStamp = parse_func()

	templateData = {
	  'button': timeStamp,
      'senPIR': timeStamp,
      'ledRed': timeStamp,
      'ledYlw': timeStamp,
      'ledGrn': timeStamp,
	}
	return render_template('index.html', **templateData)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home/node1")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    # Check if this is a message for the Pi LED.
    if msg.topic == 'home/node1':
        print("data:")
        print(msg.payload)
        # Look at the message data and perform the appropriate action.
        # if msg.payload == b'ON':
        #     pass


# Create MQTT client and connect to localhost, i.e. the Raspberry Pi running
# this script and the MQTT server.

client.on_connect = on_connect
client.on_message = on_message
client.connect('192.168.0.136', 1883, 60)
# Connect to the MQTT server and process messages in a background thread.
client.loop_start()
# Main loop to listen for button presses.
print('Script is running, press Ctrl-C to quit...')
# while True:
    # # Look for a change from high to low value on the button input to
    # time.sleep(2)  # Delay for about 20 milliseconds to debounce.
    # client.publish('home/node1', 'GET_SENSOR_DATA')

if __name__ == "__main__":
	scheduler = BackgroundScheduler()
	scheduler.add_job(parse_func, 'interval', seconds=1)
	scheduler.start()
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', port=5000, debug=True)
