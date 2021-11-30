from bs4 import BeautifulSoup
import urllib.request as req

url ="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url) 
soup = BeautifulSoup(res, 'html.parser')
# print(soup)
title = soup.find('title').string
print(title)
wf = soup.find('wf').string
print(wf)