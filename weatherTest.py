from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(response.text, 'html.parser')

table= soup.find('table', {'class':'table_develop3'})

# for tr in table.find_all('tr'):
#     tds = tr.find_all('td')
#     if len(tds) > 0:
#         print('tds[0].text(지점)=', tds[0].text)
#         print('tds[5].text(온도)=', tds[5].text)
#         print('tds[10].text(습도)=', tds[10].text)
#     print('=' * 10)

# #None 이용 : a 태그가 없으면 None 출력
# for tr in table.find_all('tr'):
#     tds = tr.find_all('td')
#     for td in tds:
#         if(td.find('a')):
#             print('a 있음')
#         else:
#             print('a 없음')

# a 가 있을 때만 지점, 온도, 습도
datas=[]
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    for td in tds:
        if(td.find('a')):
            print('tds[0].text(지점)=', tds[0].text)
            print('tds[5].text(온도)=', tds[5].text)
            print('tds[10].text(습도)=', tds[10].text)
            datas.append([tds[0].text,tds[5].text,tds[10].text])
    print('=' * 10)
print(datas)

# with open('weather.csv','w') as file:
#     print('파일저장')
#     file.write('point, temp, hum, \n')
#     for item in datas:
#         print('item=',item)
#         row= ','.join(item)
#         file.write(row+'\n')

# weather.csv 읽어 출력하기
df=pd.read_csv('weather.csv',encoding='euc-kr')
print(df)