import requests

# url = 'https://httpbin.org/post'
# files = {'file': open('payload.py', 'rb')}
#
# res = requests.post(url, files=files)
# print(res.json())
# print(res.status_code)

url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file': open('payload.py', 'rb')}

res = requests.post(url, files=files)
print(res.text)
print(res.status_code)
