import paho.mqtt.client as mqtt
from flask import Flask

app = Flask(__name__)
client = mqtt.Client()
num = 0

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

  client.publish("topic","heiheihei")
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
  client.subscribe("topic",2)

def on_message(client, userdata, msg):
	global num
	num = num + 1
	print(msg.topic+" "+str(msg.payload)+" "+str(num))

@app.route("/")
def hello():
    return "Hello World!"


client.on_connect = on_connect
client.on_message = on_message

host="guzhaoyuan.com"
client.connect(host, 1883, 60)

client.loop_forever()
