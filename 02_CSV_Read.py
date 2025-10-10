import csv

with open('01_example.csv'
          , encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)  # ข้ามหัวตาราง
    for row in reader:
        print(f"{row[0]} {row[1]} {row[2]}")


