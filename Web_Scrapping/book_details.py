import csv
from pathlib import Path

import requests
from lxml import etree
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url=url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find('div', {'class': 'side_categories'}).find('li').find('ul').find_all('li')
category = []
count = []
for i in books:
    sub_text = i.find('a').text
    sub_link = i.find('a')['href']
    response = requests.get(url=(url + sub_link))
    sub_soup = BeautifulSoup(response.content, 'html.parser')
    if sub_soup.find('form', {"class": "form-horizontal"}).find('strong'):
        sub_books_results = sub_soup.find('form', {"class": "form-horizontal"}).find('strong').text
        print(sub_text.strip(), sub_books_results.strip())
        category.append(sub_text.strip())
        count.append(sub_books_results.strip())

dic = dict(zip(category, count))
# with open(Path(__file__).parent.parent / 'batchFiles/output/output.csv', 'w', newline="") as f:
#     write = csv.writer(f).writerow(["Books", "Count"])
# for x, y in dic.items():
#     row = [x, y]
#     with open(Path(__file__).parent.parent / 'batchFiles/output/output.csv', 'a', newline="") as f:
#         write = csv.writer(f).writerow(row)

with open('output.csv', 'w', newline="") as f:
    write = csv.writer(f).writerow(["Books", "Count"])
for x, y in dic.items():
    row = [x, y]
    with open('output.csv', 'a', newline="") as f:
        write = csv.writer(f).writerow(row)
