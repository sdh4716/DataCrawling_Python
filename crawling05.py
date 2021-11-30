from bs4 import BeautifulSoup
import re
import requests
# document.querySelector("#article > div:nth-child(2) > div > div.win_result > div")
res = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin')
lotto = BeautifulSoup(res.content, 'html.parser')

ballNum = lotto.find_all('span', class_="ball_645")
# print(ballNum)
for i in ballNum:
    num = i.get_text()
    print(num, end='\t')

links = lotto.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span")

print()

for l in links:
    num = l.get_text()
    print(num, end='\t')
