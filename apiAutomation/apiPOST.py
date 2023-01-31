import secrets
import string
from time import sleep
from payload import *
import requests
from utilities.config import *
config = getConfig()

# Generate Book ID
book_id = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                  for i in range(7))

# Create Book
response = requests.post(config["API"]["host"] + "/Library/Addbook.php",
                         json=addBookPyaload(book_id)
                         , headers={"Content-Type": "application/json"}, )
assert "successfully added" in response.json()['Msg']

# Delete Book
resp = requests.post(config["API"]["host"] + "/Library/DeleteBook.php",
                     json=
                     {
                         "ID": response.json()['ID']
                     }, headers={"Content-Type": "application/json"}, )
assert resp.status_code == 200
assert "successfully deleted" in resp.json()['msg']
