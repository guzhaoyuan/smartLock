# this file publish a mqtt message to topic to the host
import paho.mqtt.publish as publish

publish.single("topic", "hello", hostname="guzhaoyuan.com")

