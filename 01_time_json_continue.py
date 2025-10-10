import json
from datetime import datetime
import os

# ข้อมูลใหม่ที่ต้องการเพิ่ม
new_entry = {
    "name": "John",
    "score": 95,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

filename = "07_example.json"

# ถ้ามีไฟล์อยู่แล้ว ให้อ่านก่อน
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        try:
            existing_data = json.load(f)
            # ถ้าเดิมเป็น dict (ไม่ใช่ list) ให้แปลงเป็น list
            if isinstance(existing_data, dict):
                existing_data = [existing_data]
        except json.JSONDecodeError:
            existing_data = []
else:
    existing_data = []

# เพิ่มข้อมูลใหม่
existing_data.append(new_entry)

# เขียนกลับลงไฟล์
with open(filename, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=4)
