import json

with open("animals_data.json", "r") as file:
    data = json.load(file)

print(data)