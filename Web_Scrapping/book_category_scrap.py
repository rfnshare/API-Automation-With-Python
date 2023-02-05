import requests
from lxml import etree
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
params = {
    "s": "ep",
    "q": "Thriller",
    "ref_": "nv_sr_sm"
}
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/109.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')
# print(obj.prettify())
# dom = etree.HTML(str(soup))
books = soup.find('div', {'class': 'side_categories'})
# print(books.prettify())
# print(dom.xpath("//div[@class='side_categories']/ul/li/ul")[].text)
rows = books.find('li').find('ul').find_all('li')

for i in rows:
    books_name = i.find('a').text
    print(books_name.strip())
    # text = links[0].text
    # print(text)



