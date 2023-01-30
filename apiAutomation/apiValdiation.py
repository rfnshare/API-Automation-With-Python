import json
import requests

response = requests.get("http://216.10.245.166/Library/GetBook.php",
                        params=
                        {
                            "AuthorName": "faroque",
                        }
                        )
# print(response.text)
# print(type(response.text))
# data = json.loads(response.text)
# print(data[0]['isbn'])
print(type(response.json()))
print(response.json()[0]['isbn'])
print(response.status_code)
