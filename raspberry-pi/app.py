from flask import Flask, render_template, request
import time
from apscheduler.schedulers.background import BackgroundScheduler
from src.mqtt_task import mqtt_task

import datetime

mqtt_task_obj = mqtt_task()
app = Flask(__name__)
scheduler = BackgroundScheduler()
data = ""

def parse_func():
    print("refresh parse_func")
    mqtt_task_obj.scheduler_task()
    timeStamp = time.time()
    return timeStamp

@app.route("/")
def home():
    for job in scheduler.get_jobs():
        job.modify(next_run_time=datetime.datetime.now())
        print("refresh start")
    
    return render_template("index.html", data=data)

@app.route("/getjson")
def json():
    file = open('static/js/data.json', "r")
    data = file.read()
    return data

@app.route("/refresh")
def refresh():
    for job in scheduler.get_jobs():
        job.modify(next_run_time=datetime.datetime.now())
    

if __name__ == "__main__":

    mqtt_task_obj.setup()
    mqtt_task_obj.scheduler_task()
    
    scheduler.add_job(parse_func, 'interval', hours=1)
    # scheduler.add_job(parse_func, 'interval', seconds=30)
    scheduler.start()
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=5000, debug=True)
