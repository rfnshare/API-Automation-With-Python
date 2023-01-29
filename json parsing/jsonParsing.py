import json

courses = '{"name": "Faroque", "languages": ["C++", "Python"]}'

data = json.loads(courses)
print(data['languages'][1])

print("************************")
# open json file from path
with open("sample.json", 'r') as f:
    data = json.load(f)

print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'][0])
