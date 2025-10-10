import json
import time
from datetime import datetime
import paho.mqtt.client as mqtt
import os

# กำหนดไฟล์ JSON
filename = "temp_data.json"
# นับจำนวนข้อมูลที่เก็บ
counter = 0
max_count = 20

# เริ่มต้นไฟล์ใหม่ (หรือโหลดของเก่า)
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data_list = json.load(f)
        except:
            data_list = []
else:
    data_list = []

# callback เมื่อมีข้อความจาก MQTT
def on_message(client, userdata, msg):
    global counter, data_list

    if counter >= max_count:
        return

    try:
        value = float(msg.payload.decode())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "sensor": "temp_1",
            "value": value,
            "unit": "°C",
            "timestamp": timestamp
        }

        data_list.append(entry)
        counter += 1

        # บันทึกลงไฟล์
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

        print(f"[{timestamp}] value: {value}")

    except Exception as e:
        print("Error:", e)

# MQTT ตั้งค่า
broker = "broker.emqx.io"  # เปลี่ยนเป็น IP ของคุณถ้าไม่ได้รันในเครื่องเดียวกัน
topic = "sensor/ldr"

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(topic)
client.loop_start()

# รับจนกว่าจะครบ 10 ค่า
while counter < max_count:
    time.sleep(1)

client.loop_stop()
client.disconnect()

print("Done. Data saved to:", filename)
