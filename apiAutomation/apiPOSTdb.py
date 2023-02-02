import secrets
import string
from time import sleep
from payload import *
import requests
from utilities.config import *
from utilities.resources import APIResources

# Get the config
config = getConfig()
headers = {"Content-Type": "application/json"}

# Create Book using DB
query = 'SELECT * FROM Books'
create_data = {
    'url': config["API"]["host"] + APIResources.addBook,
    'json': addBookPayloadFromDB(query),
    'headers': headers
}
response = requests.post(**create_data)
assert "successfully added" in response.json()['Msg']
created_id = response.json()['ID']

# Delete Book
delete_data = {
    'url': config["API"]["host"] + APIResources.deleteBook,
    'json': deleteBookPayload(created_id),
    'headers': headers
}
resp = requests.post(**delete_data)
assert resp.status_code == 200
assert "successfully deleted" in resp.json()['msg']


