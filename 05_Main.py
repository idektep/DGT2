from mqtt_module import MQTTClient
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# -------- InfluxDB Setup --------
url = "http://localhost:8086"
token = "your-token"
org = "idt"
bucket = "iot-bucket"

influx_client = InfluxDBClient(url=url, token=token, org=org)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

# -------- MQTT Callback --------
def handle_mqtt_message(client, userdata, msg):
    topic = msg.topic
    try:
        payload = float(msg.payload.decode())
        print(f"Received: {topic} → {payload}")

        parts = topic.split('/')
        if len(parts) < 2:
            print("Invalid topic format")
            return

        measurement = parts[1]  # "temperature", "humidity", "ldr"
        field_name = "value"
        field_value = payload
        tag_room = "lab1"  # สามารถทำให้ dynamic ได้ถ้าอยากแยกหลายห้อง

        point = Point(measurement).tag("room", tag_room).field(field_name, field_value)
        write_api.write(bucket=bucket, org=org, record=point)
        print("Written to InfluxDB")

    except Exception as e:
        print("Error:", e)

# -------- MQTT Start --------
topics = ["idt/temperature", "idt/humidity", "idt/ldr"]
mqtt = MQTTClient(broker="broker.emqx.io", port=1883, topics=topics, on_message_callback=handle_mqtt_message)
mqtt.start()
