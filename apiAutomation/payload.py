import secrets
import string


def addBookPyaload(book_id):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": book_id,
        "aisle": "227",
        "author": "John foe"
    }
    return body


def deleteBook():
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": id,
        "aisle": "227",
        "author": "John foe"
    }
    return body
