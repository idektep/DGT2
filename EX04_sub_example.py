import paho.mqtt.client as mqtt


# =========================
# MQTT SETUP
# =========================
broker = "broker.emqx.io"


# =========================
# TOPIC LIST
# =========================
# รับอันเดียวก็ได้
topics = [
    "scada/lv2/lab_room1/tank/level"
]




# =========================
# MQTT CALLBACK
# =========================
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    print("\n" + "=" * 50)
    print("RECEIVED DATA")
    print("TOPIC   :", topic)
    print("PAYLOAD :", payload)


# =========================
# MQTT CLIENT
# =========================
client = mqtt.Client()
client.on_message = on_message

client.connect(broker, 1883)


# =========================
# SUBSCRIBE
# =========================
for topic in topics:
    client.subscribe(topic)
    print("Subscribe:", topic)


print("-" * 50)
print("MQTT Subscriber Started")
print("-" * 50)

client.loop_forever()