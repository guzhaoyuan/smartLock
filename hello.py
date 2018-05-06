from flask import Flask
import paho.mqtt.publish as publish

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"