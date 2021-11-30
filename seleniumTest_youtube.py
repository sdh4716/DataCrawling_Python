import time
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys # END Key를 위해서 import

path = 'C:\\ChromeDriver\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = wd.Chrome(path, options=options)
#print(driver)
driver.get('https://www.youtube.com/c/paikscuisine')


body_tag = driver.find_element_by_tag_name('body')
print(body_tag)
body_tag.send_keys(Keys.END) ##스크롤이 1번 진행된다
# 화면의 길이 확인하기
# document.documentElement.scrollHeight -> 화면의 길이를 알아내는 자바스크립트
print(driver.execute_script('return document.documetElement.scrollHeight'))

while True:
    last_height = driver.execute_script('return document.documentElement.scrollHeight')
    print('last_Height = ', last_height)

    #10번 스크롤하기
    for i in range(10):
        body_tag.send_keys(Keys.END)
        time.sleep(1)
    new_height = driver.execute_script('return document.documentElement.scrollHeight')
    print('new_height = ', new_height)

    if new_height == last_height:
        print("화면 길이가 같아서 반복문 종료")
        break
    print('='*100)
    