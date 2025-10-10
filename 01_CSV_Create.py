import csv
# ข้อมูลตัวอย่าง
header = ['name', 'old', 'job']
data = [
    ['Som', 30, 'engineer'],
    ['Yi', 28, 'teacher'],
    ['Anan', 35, 'farmer']
]
# สร้างไฟล์ CSV
with open('01_example.csv', 'w', 
          newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(header)   # เขียนหัวตาราง
    writer.writerows(data)    # เขียนข้อมูลแต่ละแถว

