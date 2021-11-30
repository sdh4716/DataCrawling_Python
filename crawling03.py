from bs4 import BeautifulSoup
import re
import requests

res = requests.get('https://news.daum.net/economic#1')

soup = BeautifulSoup(res.content, 'html.parser')
# li = soup.find_all(href=re.compile(r"^https://"))

links = soup.select('a[href]')
print(len(links))
for t in links:
    if re.search('https://v.\w+',t['href']): #. 임의의 문자
        print(t.get_text().strip())          # \w 숫자와 문자
                                             # + 1회 이상