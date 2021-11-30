import requests
from bs4 import BeautifulSoup

# 영화 랭킹 가져오기
req= requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
html = req.text

soup = BeautifulSoup(html, 'html.parser')
movie_ranking_list = soup.find_all('div',class_="tit3")
# print(movie_ranking_list)
for i in range(len(movie_ranking_list)):
    print((i+1),"위",movie_ranking_list[i].get_text().strip())