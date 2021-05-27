from flask import Flask, render_template, request
import time
from apscheduler.schedulers.background import BackgroundScheduler
from src.mqtt_task import mqtt_task

# import p

mqtt_task_obj = mqtt_task()
app = Flask(__name__)
data = ""

def parse_func():
    mqtt_task_obj.scheduler_task()
    timeStamp = time.time()
    return timeStamp

@app.route("/")
def home():
    return render_template("index.html", data=data)

@app.route("/getjson")
def json():
    file = open('static/js/data.json', "r")
    data = file.read()
    return data

if __name__ == "__main__":

    mqtt_task_obj.setup()
    mqtt_task_obj.scheduler_task()
    scheduler = BackgroundScheduler()
    scheduler.add_job(parse_func, 'interval', hours=1)
    # scheduler.add_job(parse_func, 'interval', seconds=10)
    scheduler.start()
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=5000, debug=True)
