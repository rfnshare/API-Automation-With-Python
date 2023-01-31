import secrets
import string
from time import sleep

import requests

id = res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                   for i in range(7))
response = requests.post("http://216.10.245.166/Library/Addbook.php",
                         json=
                         {
                             "name": "Learn Appium Automation with Java",
                             "isbn": id,
                             "aisle": "227",
                             "author": "John foe"
                         }, headers={"Content-Type": "application/json"}, )

print(response.json())


resp = requests.post("http://216.10.245.166/Library/DeleteBook.php",
                     json=
                     {
                         "ID": response.json()['ID']
                     }, headers={"Content-Type": "application/json"}, )
print(resp.json())
assert resp.status_code == 200
