import requests
from bs4 import BeautifulSoup

res= requests.get("https://news.daum.net/digital/")
soup = BeautifulSoup(res.content, 'html.parser')

link_title = soup.find_all('a','link_txt')
# print(link_title)
print(type(link_title))

for num in range(len(link_title)):
    print(link_title[num].get_text().strip())