#### 3) Selenium을 이용한 크롤링
import re

from selenium import  webdriver as wd
from selenium.webdriver.common.keys import  Keys  # END Key를 위해서 import
from bs4 import  BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib as mpl

path = "D:\\JUNG\\util\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)

#print(driver)

# driver.get("https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA/videos")
driver.get("https://www.youtube.com/c/paikscuisine/videos")
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
#  제목과 조회수가 들어있는 dismissible을 출력하기
all_videos = soup.find_all(id='dismissible')
datas = []

for video in all_videos:
    title = video.find(id='video-title')
    video_time = video.find('span', {'class':'style-scope ytd-thumbnail-overlay-time-status-renderer'})
    video_num = video.find('span', {'class':'style-scope ytd-grid-video-renderer'})
    datas.append([title.text,video_time.text.strip(),video_num.text])




#시각화를 위해 데이터 프레임 생성
import pandas as pd
youtube = pd.DataFrame(datas, columns=('제목','재생시간','조회수'))
#print(youtube.head()) # 앞 5줄만 보여준다
print(youtube)

youtube.to_csv('recipe5.csv',mode='w',encoding='utf-8',index=True)
# with open('recipe.csv','w',encoding='utf-8') as file:
#     file.write('제목, 재생시간, 조회수\n')
#     for item in datas:
#         row = ','.join(item)
#         file.write(row+'\n')
dict_youtube = {'100만이상' :0, '50만이상' : 0, '10만이상':0}

for item in datas:
   
    item = float(str(item).split('조회수')[1].split('만회')[0].strip())
    
    if item>= 100:
        dict_youtube['100만이상'] += 1
    elif item >= 50:   
         dict_youtube['50만이상'] += 1 
    elif item >= 10:   
         dict_youtube['10만이상'] += 1      
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)
figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(dict_youtube.values(), labels=dict_youtube.keys(),autopct='%.1f%%')
plt.show()


