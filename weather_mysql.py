import requests
from bs4 import BeautifulSoup
import pymysql

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='bigdb',charset='utf8', use_unicode=True)

insert_weather ="insert into  `forecast`(`city`,`tmef`,`wf`,`tmn`,`tmx`) values(%s,%s,%s,%s,%s)"
select_last_date = "select tmef from `forecast` order by tmef desc limit 1"

req = requests.get('http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
html = req.text
soup = BeautifulSoup(html,'lxml')

cur = conn.cursor()
cur.execute(select_last_date)
last_date = cur.fetchone()
conn.commit()
# print(last_date)

weather ={}
for i in soup.find_all('location'):
    weather[i.find('city').text]=[]
    for j in i.find_all('data'):
        temp = []
        while last_date is not None:
            if tuple(j.find('tmef').text) > last_date:
                temp.append(j.find('tmef').text)
                temp.append(j.find('wf').text)
                temp.append(j.find('tmn').text)
                temp.append(j.find('tmx').text)
                weather[i.find('city').string].append(temp)
        temp.append(j.find('tmef').text)
        temp.append(j.find('wf').text)
        temp.append(j.find('tmn').text)
        temp.append(j.find('tmx').text)
        weather[i.find('city').string].append(temp)        
# print(weather.keys())
# print(weather['부산'])   
print(weather) 



for i in weather:
    for j in weather[i]:
        cur = conn.cursor()
        cur.execute(insert_weather,(i,j[0],j[1],j[2],j[3]))
        conn.commit()
