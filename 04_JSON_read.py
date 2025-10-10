import json

with open("03_example.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
