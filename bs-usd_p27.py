from bs4 import BeautifulSoup
import urllib.request as req

url ="http://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
price = soup.select_one("div.head_info > span.value").string
updown = soup.select_one("div.head_info > span.blind").string
print("usd/krw = ", price)
print("updown = ", updown)
