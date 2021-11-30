import time
from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys # END Key를 위해서 import

path = 'C:\\ChromeDriver\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = wd.Chrome(path, options=options)
#print(driver)
driver.get('https://www.youtube.com/c/paikscuisine/videos')
page = driver.page_source

soup = BeautifulSoup(page,'html.parser')
all_videos = soup.find_all(id='dismissible')
datas=[]

#metadata-line > span:nth-child(1)
for video in all_videos:
    title = video.find(id='video-title')
    video_time = video.find('span',{'class':"style-scope ytd-grid-video-renderer"})
    video_num = video.find('span',{'class':"style-scope ytd-grid-video-renderer"})
    datas.append([title.text, video_time.text.strip(), video_num.text.strip()])

# print(datas)

import pandas as pd
youtube = pd.DataFrame(datas, columns=('제목','재생시간','조회수'))
print(youtube)

youtube.to_csv('recipe5.csv',mode='w',encoding='utf-8',index=True)

dict_youtube={'100만이상' : 0, '50만이상':0, '10만이상' : 0}

import matplotlib as mpl
import matplotlib.pyplot as plt


for item in datas:
    #조회수 중에서 숫자추출
    item = float(str(item).split('조회수')[1].split('만회')[0].strip())
    # print(item)

    if item >=100:
        dict_youtube['100만이상']+=1
    elif item >=50:
        dict_youtube['50만이상']+=1 
    elif item >=10:
        dict_youtube['10만이상']+=1   
print(dict_youtube)            


font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(dict_youtube.values(), labels=dict_youtube.keys(),autopct='%.1f%%')
plt.show()