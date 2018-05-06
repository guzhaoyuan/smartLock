# this file create a mqtt server that subscribe topic from host (running in the background thread)
# meanwhile this file hosts http server that returns the number of the mqtt msgs

import paho.mqtt.client as mqtt
from flask import Flask
from threading import Thread

host="guzhaoyuan.com"
num = 0

app = Flask(__name__)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

  client.publish("topic","client connect success")
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
  client.subscribe("topic",2)

def on_disconnect(client, userdata, rc):
	if rc != 0:
		print "Desconexion inesperada al servidor MQTT COD:[{0}]".format(str(rc))

def on_message(client, userdata, msg):
	global num
	num = num + 1
	print(msg.topic+" "+str(msg.payload)+" "+str(num))

@app.route("/")
def hello():
	global num
	return str(num)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, 1883, 60)
client.loop_start()
