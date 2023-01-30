import json

with open("course.json") as f:
    data1 = json.load(f)

with open("course1.json") as f:
    data2 = json.load(f)

assert data1 == data2
