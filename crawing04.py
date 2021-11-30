from bs4 import BeautifulSoup
import re
import requests

res = requests.get('https://news.daum.net/economic#1')
soup = BeautifulSoup(res.content, 'html.parser')

# 댓글이 많은 기사 추출
links = soup.select("#cSub > div > div.section_cate.section_ranking > div.box_cate.box_bestreply")
# print(links)
# "#cSub > div > div.section_cate.section_ranking > div.box_cate.box_bestreply > ol > li:nth-child(1) > span.info_ranking"
datas = []
for t in links:
    # print(t.select_one('a.link_txt').get_text())
    # print(t.select_one('span.info_ranking').get_text())
    title = t.select_one('a.link_txt').get_text()
    count = t.select_one('span.info_ranking').get_text()
    datas.append([title,count])

print(datas)