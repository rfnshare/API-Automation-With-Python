import json

with open("course.json") as f:
    data = json.load(f)

for i in range(len(data['courses'])):
    if data['courses'][i]['title'] == "RPA":
        print(data['courses'][i]['price'])
        assert data['courses'][i]['price'] == 45
        break
