import requests
from bs4 import BeautifulSoup
import pymysql

# 1. insert

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='bigdb',charset='utf8', use_unicode=True)

insert_movie ="insert into  daummovie(moviename,moviegrade,moviereservation) values(%s,%s,%s)"


res = requests.get('https://movie.daum.net/ranking/reservation')
html = res.text
soup = BeautifulSoup(res.content, 'html.parser')
ols = soup.find('ol', class_="list_movieranking")
rankcont = ols.find_all('div', class_="thumb_cont")

cur = conn.cursor()
for i in rankcont:
    moviename = i.find('a',class_="link_txt").get_text()
    moviegrade = i.find('span', class_="txt_grade").text.strip()
    movieReser = i.find('span',{'class':'txt_num'}).text.strip()
    # print(moviename,moviegrade,movieReser)
    # cur.execute(insert_movie,(moviename,moviegrade,movieReser))
    # conn.commit()

# 2. title, grade 평점이 높은 순으로 평점이 같다면 
# title을 오름차순으로 5개 출력
select_movie ="select moviename, moviegrade from  daummovie order by moviegrade desc, moviename asc limit 1, 5"
cur.execute(select_movie)
movies = cur.fetchall()
print(movies)
print(type(movies))

# 평점이 9점이상, 8점이상, 6점이상, 6점미만 ==> pie
select_movie1 = "select moviegrade, count(*) from daummovie group by moviegrade"
# select_movie1 ="select moviegrade from daummovie"
cur.execute(select_movie1)
movies1 = cur.fetchall()

dict_movie = {'9점 이상' : 0, '8점 이상' : 0, '6점 이상' : 0, '6점 미만' : 0}

for item in movies1:
    # 만약 평점을 str로 했다면 
    # movie = float(movie[0]) 이런식으로 형변환을 해줘야 함
    if item[0] >= 9:
        # dict_movie['9점 이상']+=1
        dict_movie['9점 이상']+=item[1]
    elif item[0] >=8:
        # dict_movie['8점 이상']+=1
        dict_movie['8점 이상']+=item[1]
    elif item[0] >=6:
        # dict_movie['6점 이상']+=1
        dict_movie['6점 이상']+=item[1]
    else:
        # dict_movie['6점 미만']+=1
        dict_movie['6점 미만']+=item[1]
print(dict_movie)

import matplotlib as mpl
import matplotlib.pyplot as plt
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(dict_movie.values(), labels=dict_movie.keys(),autopct='%.1f%%')
plt.show()
