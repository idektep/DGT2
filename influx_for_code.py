import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# ----------- InfluxDB Config -----------
url = "http://localhost:8086"
token = "1F7EVZ2j8z7zo5SlSWDcLv_k007b793zY3ykZt1T-ARbI7sd-jlibeDbEtCB1c7lblXYHEI8__fJsLXxH53x5g=="
org = "idt"
bucket = "iot-bucket"

influx_client = InfluxDBClient(url=url, token=token, org=org)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

# ----------- MQTT Config -----------
mqtt_broker = "broker.emqx.io"
mqtt_port = 1883

subscribe_topics = [
    "traffic_sim/n/car",
    "traffic_sim/e/car",
    "traffic_sim/s/car",
    "traffic_sim/w/car",
    "traffic_sim/n/lamp",
    "traffic_sim/e/lamp",
    "traffic_sim/s/lamp",
    "traffic_sim/w/lamp",
]

# ----------- Callback Functions -----------
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code", rc)
    for topic in subscribe_topics:
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload_str = msg.payload.decode().strip()
    print(f"Received: {topic} → {payload_str}")

    try:
        # CAR COUNT
        if topic == "traffic_sim/n/car":
            value = int(payload_str)
            point = Point("traffic_car").tag("direction", "n").field("value", value)

        elif topic == "traffic_sim/e/car":
            value = int(payload_str)
            point = Point("traffic_car").tag("direction", "e").field("value", value)

        elif topic == "traffic_sim/s/car":
            value = int(payload_str)
            point = Point("traffic_car").tag("direction", "s").field("value", value)

        elif topic == "traffic_sim/w/car":
            value = int(payload_str)
            point = Point("traffic_car").tag("direction", "w").field("value", value)

        # LAMP STATE
        elif topic == "traffic_sim/n/lamp":
            mapped_value = {"red": 0, "yellow": 1, "green": 2}.get(payload_str.lower(), -1)
            point = Point("traffic_lamp_state").tag("direction", "n").field("state", mapped_value)

        elif topic == "traffic_sim/e/lamp":
            mapped_value = {"red": 0, "yellow": 1, "green": 2}.get(payload_str.lower(), -1)
            point = Point("traffic_lamp_state").tag("direction", "e").field("state", mapped_value)

        elif topic == "traffic_sim/s/lamp":
            mapped_value = {"red": 0, "yellow": 1, "green": 2}.get(payload_str.lower(), -1)
            point = Point("traffic_lamp_state").tag("direction", "s").field("state", mapped_value)

        elif topic == "traffic_sim/w/lamp":
            mapped_value = {"red": 0, "yellow": 1, "green": 2}.get(payload_str.lower(), -1)
            point = Point("traffic_lamp_state").tag("direction", "w").field("state", mapped_value)

        else:
            print("Unknown topic:", topic)
            return

        # Write to InfluxDB
        write_api.write(bucket=bucket, org=org, record=point)
        print("✅ Written to InfluxDB")

    except Exception as e:
        print("⚠️ Error:", e)

# ----------- Start MQTT Client -----------
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(mqtt_broker, mqtt_port, 60)
mqtt_client.loop_forever()
