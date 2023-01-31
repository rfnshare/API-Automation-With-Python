import requests

res = requests.get('https://api.github.com/users/rfnshare', verify=True, auth=('user', 'pass'))
print(res.status_code)
print(res.json()['company'])