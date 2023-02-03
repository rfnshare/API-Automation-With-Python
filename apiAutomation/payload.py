import secrets
import string

from utilities.config import getQuery


def addBookPayload(book_id, aisle):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": book_id,
        "aisle": aisle,
        "author": "John foe"
    }
    return body


def deleteBookPayload(book_id):
    body = {
        "ID": book_id,
    }
    return body


def addBookPayloadFromDB(query):
    add_body = {}
    tp = getQuery(query)
    add_body['name'] = tp[0]
    add_body['isbn'] = tp[1]
    add_body['aisle'] = tp[2]
    add_body['author'] = tp[3]
    return add_body
