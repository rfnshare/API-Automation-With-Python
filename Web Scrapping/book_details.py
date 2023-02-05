import requests
from lxml import etree
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url=url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find('div', {'class': 'side_categories'}).find('li').find('ul').find_all('li')
for i in books:
    sub_text = i.find('a').text
    sub_link = i.find('a')['href']
    response = requests.get(url=(url + sub_link))
    sub_soup = BeautifulSoup(response.content, 'html.parser')
    sub_books_results = sub_soup.find('form', {"class": "form-horizontal"}).find('strong').text
    print(sub_text.strip(), sub_books_results.strip())
