import json
from datetime import datetime

# สร้างข้อมูล
data = {
    "name": "John",
    "score": 95,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# เขียนลงไฟล์ JSON
with open("07_example.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



