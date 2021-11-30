from bs4 import BeautifulSoup
import re
from openpyxl import Workbook
import requests

res = requests.get('https://finance.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')

# document.querySelector("#container > div.aside > div > div.aside_area.aside_popular > table > tbody")

tbody = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular > table > tbody")
trs =tbody.select('tr')
# print(trs)

datas = []
for tr in trs:
    name = tr.select_one('th > a').get_text()
    curr_price = tr.select_one('td').get_text()
    ch_direction = tr['class'][0]
    ch_price = tr.select_one('td > span').get_text().strip()
    datas.append([name, curr_price, ch_direction, ch_price])

print(datas)

write_wb = Workbook()
write_ws = write_wb.create_sheet('결과')
for data in datas:
    write_ws.append(data)

write_wb.save(r'testsave.xlsx')