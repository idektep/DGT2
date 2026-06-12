import random
from datetime import datetime
import tkinter as tk


# =========================
# สร้างหน้าต่าง UI
# =========================
root = tk.Tk()
root.title("Week 2 - Raw Data Generator with Image Layout")
root.geometry("850x750")


# =========================
# หัวข้อ
# =========================
title = tk.Label(root, text="Raw Data Generator + 2D Image Layout", font=("Arial", 20, "bold"))
title.pack(pady=10)


# =========================
# Frame หลักสำหรับรูป
# =========================
main_frame = tk.Frame(root)
main_frame.pack(pady=10)


# =========================
# Tank
# =========================
tank_label = tk.Label(main_frame)
tank_label.image = tk.PhotoImage(file="week02/pic/tank1.png")
tank_label.config(image=tank_label.image)
tank_label.grid(row=0, column=0, padx=35, pady=10)

tank_text = tk.Label(main_frame, text="Tank Level: -", font=("Arial", 14))
tank_text.grid(row=1, column=0)

tank_status_text = tk.Label(main_frame, text="Status: -", font=("Arial", 12))
tank_status_text.grid(row=2, column=0)


# =========================
# Lamp
# =========================
lamp_label = tk.Label(main_frame)
lamp_label.image = tk.PhotoImage(file="week02/pic/lamp1.png")
lamp_label.config(image=lamp_label.image)
lamp_label.grid(row=0, column=1, padx=35, pady=10)

lamp_text = tk.Label(main_frame, text="Lamp Status: -", font=("Arial", 14))
lamp_text.grid(row=1, column=1)


# =========================
# Fan
# =========================
fan_label = tk.Label(main_frame)
fan_label.image = tk.PhotoImage(file="week02/pic/fan1.png")
fan_label.config(image=fan_label.image)
fan_label.grid(row=3, column=0, padx=35, pady=10)

fan_text = tk.Label(main_frame, text="Fan Speed: -", font=("Arial", 14))
fan_text.grid(row=4, column=0)


# =========================
# Machine
# =========================
machine_label = tk.Label(main_frame)
machine_label.image = tk.PhotoImage(file="week02/pic/machine1.png")
machine_label.config(image=machine_label.image)
machine_label.grid(row=3, column=1, padx=35, pady=10)

machine_text = tk.Label(main_frame, text="Machine Alarm: -", font=("Arial", 14))
machine_text.grid(row=4, column=1)


# =========================
# ข้อความเวลา
# =========================
time_text = tk.Label(root, text="Time: -", font=("Arial", 12))
time_text.pack(pady=5)


# =========================
# ฟังก์ชันสุ่มข้อมูลทั้งหมด + Update UI
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
    # เปลี่ยนรูปเฉพาะ Tank ก่อน
    # =========================
    if lab_room1_tank_level > 80:
        tank_label.image = tk.PhotoImage(file="week02/pic/tank3.png")
        tank_label.config(image=tank_label.image)
        tank_status = "HIGH"

    elif lab_room1_tank_level > 50:
        tank_label.image = tk.PhotoImage(file="week02/pic/tank2.png")
        tank_label.config(image=tank_label.image)
        tank_status = "MEDIUM"

    else:
        tank_label.image = tk.PhotoImage(file="week02/pic/tank1.png")
        tank_label.config(image=tank_label.image)
        tank_status = "LOW"


    # =========================
    # Update ข้อความบน Layout
    # =========================
    tank_text.config(text=f"Tank Level: {lab_room1_tank_level}%")
    tank_status_text.config(text=f"Status: {tank_status}")

    lamp_text.config(text=f"Lamp Status: {lab_room1_lamp_status}")
    fan_text.config(text=f"Fan Speed: {lab_room1_fan_speed}%")
    machine_text.config(text=f"Machine Alarm: {machine01_alarm}")

    time_text.config(text=f"Time: {current_time}")


    # =========================
    # Loop ทุก 1 วินาที
    # =========================
    root.after(1000, update_data)


# =========================
# Start Program
# =========================
update_data()
root.mainloop()