from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib as mpl

# 권한이 따로 설정되어 추출이 안되는 사이트의 경우 되는 권한으로 추출
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
res = requests.get('https://news.naver.com/main/home.naver',headers=header)
html = res.text
soup = BeautifulSoup(res.content, 'html.parser')

#main_content > div

main = soup.select_one('#main_content > div')

# {} = dictionary / java에서의 map (key, value)
# 데이터 갯수 구하기
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/Hancom Gothic Bold.ttf').get_name()
mpl.rc('font', family=font_name)

news = {}
newspaper = main.find_all('span', class_="writing")
for i in newspaper:
    if(news.get(i.string)==None):
        news[i.string] = 1
    else:
        news[i.string] += 1
print(news)
figure = plt.figure()
axes = figure.add_subplot(111)

axes.pie(news.values(), labels=news.keys(), autopct='%.1f%%')
plt.show()