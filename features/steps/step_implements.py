import secrets
import string

import requests
from behave import *

from apiAutomation.payload import addBookPayload
from utilities.config import *
from utilities.resources import APIResources
from utilities.secrects import Info

config = getConfig()


@given('the book details which needs to be added to library')
def step_impl(context):
    context.book_id = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                              for i in range(7))
    context.headers = {"Content-Type": "application/json"}
    context.url = config["API"]["host"] + APIResources.addBook
    context.payload = addBookPayload(context.book_id, "227")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    context.book_id = context.response.json()['ID']
    print(context.book_id)
    assert "successfully added" in context.response.json()['Msg']


@given(u'the book details with {isbn} & {aisle}')
def step_impl(context, isbn, aisle):
    context.headers = {"Content-Type": "application/json"}
    context.url = config["API"]["host"] + APIResources.addBook
    context.payload = addBookPayload(isbn, aisle)


@given('I Have Github Auth Credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = ('rfnshare', Info.token)


@when('I Hit GitRepo API of Github')
def step_impl(context):
    context.response = context.se.get(APIResources.github_repo)


@then('Status Code of response should be {status_code:d}')
def step_impl(context, status_code):
    print(context.response.status_code)
    assert context.response.status_code == status_code
