import requests

url = "https://rahulshettyacademy.com"
res = requests.get(url, allow_redirects=False, timeout=2)
print(res.history)
print(res.status_code)
