import secrets
import string


def addBookPayload(book_id):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": book_id,
        "aisle": "227",
        "author": "John foe"
    }
    return body


def deleteBookPayload(book_id):
    body = {
        "ID": book_id,
    }
    return body
