import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = "http://localhost:8086"
token = "your token"
org = "your org"
bucket = "your bucket"
influx_client = InfluxDBClient(url=url, token=token, org=org)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

# ----------- MQTT Config -----------
mqtt_broker = "broker.emqx.io"
mqtt_port = 1883
subscribe_topics = [
    "______/sensor/ldr",
    "______/sensor/temp",
    "______/sensor/humid"
]

# ----------- Callback Functions -----------
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code", rc)
    for topic in subscribe_topics:
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")

def on_message(client, userdata, msg):
    topic = msg.topic
    try:
        payload = float(msg.payload.decode())
        print(f"Received: {topic} → {payload}")

        if topic == "______/sensor/ldr":
            point = Point("esp32 device").tag("sensor", "ldr").field("value", payload)

        elif topic == "______/sensor/temp":
            point = Point("esp32 device").tag("sensor", "temp").field("value", payload)

        elif topic == "______/sensor/humid":
            point = Point("esp32 device").tag("sensor", "humid").field("value", payload)

        else:
            print("Unknown topic:", topic)
            return

        write_api.write(bucket=bucket, org=org, record=point)
        print("Written to InfluxDB")

    except Exception as e:
        print("Error:", e)

# ----------- Start MQTT Client -----------
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(mqtt_broker, mqtt_port, 60)
mqtt_client.loop_forever()
