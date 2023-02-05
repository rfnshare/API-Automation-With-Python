from bs4 import BeautifulSoup
import requests

url = "https://www.rahulshettyacademy.com/AutomationPractice/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
web_table = soup.find('table', {'id': 'product'}).find_all('tr')
for i in web_table[1:]:
    course = i.find_all('td')
    print(course[1].text)

all_links = soup.find('div', {'id': 'gf-BIG'}).find_all('a')
for i in all_links:
    if i['href'] != '#':
        print(i['href'])

appium_link = soup.find('a', string='Appium')
print(appium_link['href'])
