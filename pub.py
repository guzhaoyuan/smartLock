import paho.mqtt.publish as publish


publish.single("topic", "hello", hostname="guzhaoyuan.com")

