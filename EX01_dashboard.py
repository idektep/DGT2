import random
from datetime import datetime
import tkinter as tk


# =========================
# สร้างหน้าต่าง UI แค่ครั้งเดียว
# =========================
root = tk.Tk()
root.title("Show Image in Python UI")
root.geometry("500x600")


# =========================
# โหลดรูปแค่ครั้งเดียว
# =========================
tank1 = tk.PhotoImage(file="week02/pic/tank1.png")
tank2 = tk.PhotoImage(file="week02/pic/tank2.png")
tank3 = tk.PhotoImage(file="week02/pic/tank3.png")


# =========================
# สร้าง UI แค่ครั้งเดียว
# =========================
image_label = tk.Label(root, image=tank1)
image_label.pack(pady=20)

text_label = tk.Label(root, text="Tank Object", font=("Arial", 16))
text_label.pack()

level_label = tk.Label(root, text="lab_room1_tank_level = -", font=("Arial", 14))
level_label.pack(pady=5)

status_label = tk.Label(root, text="Status: -", font=("Arial", 14))
status_label.pack(pady=5)

time_label = tk.Label(root, text="Time: -", font=("Arial", 12))
time_label.pack(pady=5)


# =========================
# ฟังก์ชันสุ่มข้อมูล + update รูป
# =========================
def update_data():
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
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 60)
    print("RAW DATA TIME:", current_time)
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


    # =========================
    # CHANGE IMAGE BY CONDITION
    # =========================
    if lab_room1_tank_level > 80:
        image_label.config(image=tank3)
        tank_status = "HIGH"

    elif lab_room1_tank_level > 50:
        image_label.config(image=tank2)
        tank_status = "MEDIUM"

    else:
        image_label.config(image=tank1)
        tank_status = "LOW"


    # =========================
    # UPDATE TEXT ON UI
    # =========================
    level_label.config(text=f"lab_room1_tank_level = {lab_room1_tank_level}")
    status_label.config(text=f"Status: {tank_status}")
    time_label.config(text=f"Time: {current_time}")


    # =========================
    # LOOP EVERY 1 SECOND
    # =========================
    root.after(1000, update_data)


# เริ่มทำงานครั้งแรก
update_data()

# เปิด UI ค้างไว้
root.mainloop()