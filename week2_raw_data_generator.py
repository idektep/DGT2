import random
import time
from datetime import datetime


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
    # PRINT RAW DATA
    # =========================
    print("\n" + "=" * 60)
    print("RAW DATA TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 60)

    print("lab_room1_tank_temp       =", lab_room1_tank_temp)
    print("lab_room1_tank_level      =", lab_room1_tank_level)
    print("lab_room1_tank_pump       =", lab_room1_tank_pump)
    print("lab_room1_fan_speed       =", lab_room1_fan_speed)
    print("lab_room1_fan_status      =", lab_room1_fan_status)
    print("lab_room1_lamp_status     =", lab_room1_lamp_status)
    print("lab_room1_alarm           =", lab_room1_alarm)

    print("lab_room2_tank_temp       =", lab_room2_tank_temp)
    print("lab_room2_level           =", lab_room2_level)
    print("lab_room2_pump_status     =", lab_room2_pump_status)
    print("lab_room2_motor_speed     =", lab_room2_motor_speed)
    print("lab_room2_motor_run       =", lab_room2_motor_run)
    print("lab_room2_warning_light   =", lab_room2_warning_light)
    print("lab_room2_alarm_status    =", lab_room2_alarm_status)

    print("station_temp              =", station_temp)
    print("station_humidity          =", station_humidity)
    print("station_emergency         =", station_emergency)
    print("station_mode              =", station_mode)
    print("station_conveyor_speed    =", station_conveyor_speed)
    print("station_conveyor_run      =", station_conveyor_run)
    print("station_sensor_count      =", station_sensor_count)

    print("machine01_temp            =", machine01_temp)
    print("machine01_motor           =", machine01_motor)
    print("machine01_alarm           =", machine01_alarm)
    print("machine01_vibration       =", machine01_vibration)

    print("machine02_temp            =", machine02_temp)
    print("machine02_motor_status    =", machine02_motor_status)
    print("machine02_alarm_status    =", machine02_alarm_status)
    print("machine02_pressure        =", machine02_pressure)

    time.sleep(1)