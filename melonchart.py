from bs4 import BeautifulSoup
import requests
import re

# 권한이 따로 설정되어 추출이 안되는 사이트의 경우 되는 권한으로 추출
header={'User-Agent': 'Mozilla/5.0'}
res = requests.get('https://www.melon.com/chart/week/index.htm',headers=header)
html = res.text
soup = BeautifulSoup(res.content, 'html.parser')
#frm > div > table > tbody
tbody = soup.select_one("#frm > div > table > tbody")
# print(chart)
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
#frm > div > table > tbody
#lst50
trs = tbody.select('tr#lst50')
datas=[]
for tr in trs:
    #lst50 > td:nth-child(2) > div > span.rank
    rank = tr.select_one('span.rank').get_text()
    #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01
    name = re.sub('\n','',tr.select_one('div.rank01').get_text())
    name = name.replace(',',' ')
    #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02
    # div의 이름으로 가져올 때
    singer = re.sub('\n','',tr.select_one('div.rank02').get_text())
    #lst50 > td:nth-child(7) > div > div > div > a
    # a태그를 그대로 가져올 때
    album = tr.select_one('div.rank03 > a').get_text()

    # re.sub로 성가신 '\n'값을 없애고 가져온다

    datas.append([rank,name,singer,album])

print(datas)

# melon.csv로 출력

with open('melon.csv','w') as file:
    file.write('순위, 곡명, 가수, 앨범\n')
    for item in datas:
        row = ','.join(item)
        file.write(row+'\n')