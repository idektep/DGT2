import random
import time
from datetime import datetime
import paho.mqtt.client as mqtt


# =========================
# MQTT SETUP
# =========================
broker = "broker.emqx.io"

client = mqtt.Client()
client.connect(broker, 1883)



while True:
    # =========================
    # RAW DATA FROM LAB ROOM 1
    # =========================
    lab_room1_tank_temp = round(random.uniform(25.0, 45.0), 2)
    lab_room1_tank_level = random.randint(0, 100)
    lab_room1_tank_pump = random.choice([0, 1])

    lab_room1_fan_speed = random.randint(0, 100)
    lab_room1_fan_status = random.choice([0, 1])

    lab_room1_lamp_status = random.choice([0, 1])
    lab_room1_alarm = random.choice([0, 0, 0, 1])


    # =========================
    # RAW DATA FROM LAB ROOM 2
    # =========================
    lab_room2_tank_temp = round(random.uniform(25.0, 50.0), 2)
    lab_room2_level = random.randint(0, 100)
    lab_room2_pump_status = random.choice([0, 1])

    lab_room2_motor_speed = random.randint(0, 1500)
    lab_room2_motor_run = random.choice([0, 1])

    lab_room2_warning_light = random.choice([0, 1])
    lab_room2_alarm_status = random.choice([0, 0, 0, 1])


    # =========================
    # RAW DATA FROM STATION
    # =========================
    station_temp = round(random.uniform(24.0, 40.0), 2)
    station_humidity = random.randint(40, 90)
    station_emergency = random.choice([0, 0, 0, 1])
    station_mode = random.choice(["auto", "manual"])

    station_conveyor_speed = random.randint(0, 100)
    station_conveyor_run = random.choice([0, 1])
    station_sensor_count = random.randint(0, 999)


    # =========================
    # RAW DATA FROM MACHINE AREA
    # =========================
    machine01_temp = round(random.uniform(30.0, 75.0), 2)
    machine01_motor = random.choice([0, 1])
    machine01_alarm = random.choice([0, 0, 0, 1])
    machine01_vibration = round(random.uniform(0.0, 5.0), 2)

    machine02_temp = round(random.uniform(30.0, 80.0), 2)
    machine02_motor_status = random.choice([0, 1])
    machine02_alarm_status = random.choice([0, 0, 0, 1])
    machine02_pressure = round(random.uniform(0.0, 10.0), 2)


    # =========================
    # MQTT PUBLISH EXAMPLE
    # =========================
    # จากตัวแปรดิบ:
    # lab_room1_tank_level
    #
    # แปลงเป็น hierarchy:
    # scada/lv2/lab_room1/tank/level

    client.publish("scada/lv2/lab_room1/tank/level", lab_room1_tank_level)


    time.sleep(1)