import requests
from utilities.secrects import Info

se = requests.session()
se.auth = auth = ('rfnshare', Info.token)

res = se.get('https://api.github.com/user')
print(res.status_code)
print(res.json()['company'])

res2 = se.get('https://api.github.com/user/repos')
print(res2.status_code)
