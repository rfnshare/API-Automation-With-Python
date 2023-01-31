import requests

response = requests.post("http://216.10.245.166/Library/Addbook.php",
                         json=
                         {
                             "name": "Learn Appium Automation with Java",
                             "isbn": "bcd234872",
                             "aisle": "227",
                             "author": "John foe"
                         }, headers={"Content-Type": "application/json"},)

print(response.status_code)
print(response.json()['ID'])
