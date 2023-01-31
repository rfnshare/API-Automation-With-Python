import json
import requests

from utilities.config import *
from utilities.resources import APIResources
config = getConfig()

# Get BookList By Author
response = requests.get(config["API"]["host"]+APIResources.getBook,
                        params=
                        {
                            "AuthorName": "Rahul Shetty",
                        }
                        )
# print(response.text)
# print(type(response.text))
# data = json.loads(response.text)
# print(data[0]['isbn'])
# print(type(response.json()))
# print(response.json()[0]['isbn'])
assert response.status_code == 200
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# print(type(response.json()))
actual_book = None
for i in response.json():
    if i['isbn'] == 'RGHCC':
        actual_book = i
        break
expected_book = {'book_name': 'Learn with Java', 'isbn': 'RGHCC', 'aisle': '222'}
assert actual_book == expected_book

