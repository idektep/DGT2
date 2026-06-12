import tkinter as tk

# สร้างหน้าต่าง UI
root = tk.Tk()
root.title("Show 4 Images in Python UI")
root.geometry("700x600")

# โหลดรูป
tank_image = tk.PhotoImage(file="week02/pic/tank1.png")
lamp_image = tk.PhotoImage(file="week02/pic/lamp1.png")
fan_image = tk.PhotoImage(file="week02/pic/fan1.png")
machine_image = tk.PhotoImage(file="week02/pic/machine1.png")

# หัวข้อ
title = tk.Label(root, text="Python 2D Object Layout", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Frame หลักสำหรับวางรูป
main_frame = tk.Frame(root)
main_frame.pack(pady=10)

# รูปที่ 1: Tank
tank_label = tk.Label(main_frame, image=tank_image)
tank_label.grid(row=0, column=0, padx=30, pady=20)

tank_text = tk.Label(main_frame, text="Tank", font=("Arial", 14))
tank_text.grid(row=1, column=0)

# รูปที่ 2: Lamp
lamp_label = tk.Label(main_frame, image=lamp_image)
lamp_label.grid(row=0, column=1, padx=30, pady=20)

lamp_text = tk.Label(main_frame, text="Lamp", font=("Arial", 14))
lamp_text.grid(row=1, column=1)

# รูปที่ 3: Fan
fan_label = tk.Label(main_frame, image=fan_image)
fan_label.grid(row=2, column=0, padx=30, pady=20)

fan_text = tk.Label(main_frame, text="Fan", font=("Arial", 14))
fan_text.grid(row=3, column=0)

# รูปที่ 4: Machine
machine_label = tk.Label(main_frame, image=machine_image)
machine_label.grid(row=2, column=1, padx=30, pady=20)

machine_text = tk.Label(main_frame, text="Machine", font=("Arial", 14))
machine_text.grid(row=3, column=1)

# เปิดหน้าต่างค้างไว้
root.mainloop()