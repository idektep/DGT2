import json

# Data as a list of dictionaries
people = [
    {"name": "John", "age": 30, "occupation": "Engineer"},
    {"name": "Mary", "age": 28, "occupation": "Teacher"}
]

# Write to JSON file
with open("03_example.json", "w", encoding="utf-8") as f:
    json.dump(people, f, indent=4)
