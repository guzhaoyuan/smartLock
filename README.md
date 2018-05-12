# smartLock

## 测试环境

Ubuntu14.04/Mac Python2.7.9+

## 目前需求

- 一个mqtt server, 用于接收传感器类似物的数据
- 一个http server, 用于通过网页返回传感器的某些数据

## 文件介绍

- client.py 单独的mqtt server，可以发送和接收mqtt包
- pub.py 单独的发送mqtt的包
- hello.py 一个demo的http server
- server.py 同时接收mqtt消息, 起一个http server, 返回接收到的mqtt包数量

## 使用方法

1.安装mqtt server端软件(这些主要是用命令行玩mqtt，方便理解和调试用的)

	sudo apt-get update
	sudo apt-get install mosquitto mosquitto-clients

按照DO上的教程把mqtt server配置好，主要是修改配置文件，增加mqtt user并设置密码，然后

	mosquitto -c /etc/mosquitto/mosquitto.conf
	mosquitto_sub -t "topic/#"	#in another terminal

就可以在客户端上跑起来了


2.安装flask, paho-mqtt

	pip install flask
	pip install paho-mqtt
	export FLASK_APP=server.py
	python -m flask run —host=0.0.0.0#flask语法，=run server.py, host默认是127.0.0.1,需要手动改为接受所有ip的请求

访问 your_ip:5000 可以看到收到的mqtt包的数目

3.尝试玩耍

	mosquitto_pub -t "topic" -h localhost -m "nihao"

这就是通过命令行给topic发信息，再次刷新your_ip:5000可以看到数字改变

4.进一步修改程序
可以在这个框架下，接收任何mqtt发送的数据，然后再通过一个好看的网页显示，下面的[某可以借鉴的github项目](https://github.com/neubatengog/FlaskMqtt/blob/master/server.py)还用到了socketio,之后可以尝试玩耍。

## 相关文档

[DO上搭建mqtt server的教程](https://www.digitalocean.com/community/questions/how-to-setup-a-mosquitto-mqtt-server-and-receive-data-from-owntracks)

[flask文档](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)

[pypi mqtt库文档](https://pypi.org/project/paho-mqtt/#usage-and-api)

[某可以借鉴的github项目](https://github.com/neubatengog/FlaskMqtt/blob/master/server.py)