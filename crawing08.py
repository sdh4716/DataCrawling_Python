from bs4 import BeautifulSoup
import requests

res = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20211115')
html = res.text
soup = BeautifulSoup(res.content, 'html.parser')

#old_content > table > tbody > tr:nth-child(2) > td.title > div

#old_content > table > tbody
#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(2) > td.point
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
tbody = soup.select_one("#old_content > table > tbody")
trs = tbody.select("tr")
# print(trs)
datas=[]
for tr in trs:
    name = tr.select_one('div.tit5 > a')
    if(name !=None):
        print(name.get_text())
    rating = tr.select_one('td.point')
    if(rating !=None):
        print(rating.get_text())
print(datas)


