import tkinter as tk

# สร้างหน้าต่าง UI
root = tk.Tk()
root.title("Show Image in Python UI")
root.geometry("500x500")

# โหลดรูป
tank_image = tk.PhotoImage(file="week02/pic/tank1.png")

# แสดงรูปบนหน้าจอ
image_label = tk.Label(root, image=tank_image)
image_label.pack(pady=20)

# ข้อความใต้รูป
text_label = tk.Label(root, text="Tank Object", font=("Arial", 16))
text_label.pack()

# เปิดหน้าต่างค้างไว้
root.mainloop()