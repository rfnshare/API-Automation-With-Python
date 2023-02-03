import requests

from apiAutomation.payload import deleteBookPayload
from utilities.config import getConfig
from utilities.resources import APIResources

config = getConfig()
headers = {"Content-Type": "application/json"}


def before_scenario(context, scenario):
    print("Welcome To Hogwarts")


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        resp = requests.post(config["API"]["host"] + APIResources.deleteBook, json=deleteBookPayload(context.book_id),
                             headers=headers, )
        print("Deleted:", context.book_id)
        assert resp.status_code == 200
        assert "successfully deleted" in resp.json()['msg']
