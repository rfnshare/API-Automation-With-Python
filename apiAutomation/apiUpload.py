import requests

url = 'https://httpbin.org/post'
files = {'file': open('payload.py', 'rb')}

res = requests.post(url, files=files)
print(res.json())
print(res.status_code)