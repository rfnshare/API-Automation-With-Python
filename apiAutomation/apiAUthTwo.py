import requests

# url = "https://rahulshettyacademy.com/"
# cookie = {'visit-month': 'February'}
# res = requests.get(url, cookies=cookie)
# print(res.status_code)
se = requests.session()
url = "https://httpbin.org/cookies"
se.cookies.update({'visit-month': 'February', 'visit-year': '2022'})
res = se.get(url)
print(res.status_code)
print(res.json())

