import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

broker = "broker.emqx.io"
client = mqtt.Client()
client.on_message = on_message
client.connect(broker, 1883)

# Subscribe ด้วย wildcard
client.subscribe("xv1/+/temp")  # จะจับได้ your_topic1/livingroom/temp, your_topic1/kitchen/temp
client.subscribe("xv2/#")    # จะจับได้ทุกหัวข้อที่ขึ้นต้นด้วย factory/

client.loop_forever()
