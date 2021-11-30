from bs4 import BeautifulSoup
import requests

res = requests.get('https://movie.daum.net/ranking/reservation')
html = res.text
soup = BeautifulSoup(res.content, 'html.parser')

ols = soup.find('ol', class_="list_movieranking")
rankcont = ols.find_all('div', class_="thumb_cont")


for i in rankcont:
    moviename = i.find('a',class_="link_txt").get_text()
    moviegrade = i.find('span', class_="txt_grade").text.strip()
    movieReser = i.find('span',{'class':'txt_num'}).text.strip()
    print(moviename)
    print('평점',moviegrade)
    print('예약률 :',movieReser)
    print()