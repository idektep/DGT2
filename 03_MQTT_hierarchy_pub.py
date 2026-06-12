import time
import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
client = mqtt.Client()
client.connect(broker, 1883)

while True:
    client.publish("dgt/factory/temp", "28.5")
    client.publish("dgt/factory/humidity", "80")
    client.publish("dgt/factory/light", "123")
    client.publish("dgt/livingroom/temp", "28.5")
    client.publish("dgt/livingroom/humi", "80")
    client.publish("dgt/kitchen/temp", "30.1")
    client.publish("dgt/line1/status", "OK")
    time.sleep(2)
