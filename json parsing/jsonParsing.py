import json

courses = '{"name": "Faroque", "languages": ["C++", "Python"]}'

data = json.loads(courses)
print(data['languages'][1])
