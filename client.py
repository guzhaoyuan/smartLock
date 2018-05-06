import paho.mqtt.client as mqtt
from flask import Flask
from threading import Thread

host="guzhaoyuan.com"
num = 0

app = Flask(__name__)
mqtt_thread = None

class MQTT_Thread(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.stop = False

	def run(self):
		while not self.stop and client.loop_forever() == 0:
			pass
		print "MQTT Thread terminado"


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

# def main():
	# try:
	# 	mqtt_thread = MQTT_Thread()
	# 	mqtt_thread.start()

	# except Exception, e:
	# 	client.disconnect
	# 	client.reconnect()
	# 	print "Error:{0} ".format(str(e))


# if __name__ == '__main__':main()

client.loop_start()
