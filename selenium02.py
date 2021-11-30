from selenium import webdriver as wd

#p74,75
# 페이지 소스 보기에 없는 코드들은 값을 가져올 수 없기 때문에
# 동적으로 직접 작동을 시킨 후 데이터를 추출한다.

# \는 무조건 \\ 두번
path ='C:\\ChromeDriver\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = wd.Chrome(path, options=options)
driver.get('https://tour.interpark.com')
# print(driver)
#복수개가 필요할때는 find_elements
driver.find_element_by_id('SearchGNBText').send_keys('스위스') #send_keys:키보드 입력
driver.find_element_by_class_name('search-btn').click() #click 마우스 클릭
driver.implicitly_wait(10)
driver.find_element_by_id('li_R').click()
driver.implicitly_wait(10)
import time
for page in range(1,8):
    driver.execute_script("searchModule.SetCategoryList({},'')".format(page))
    time.sleep(3)
    # page에 해당하는 값이 앞 중괄호로 들어감
    print(str(page)+"번째 페이지") #str = 문자로 만듦
    boxItems= driver.find_elements_by_css_selector(".panelZone>.oTravelBox>.boxList>li")

for li in boxItems:
    print('제목', li.find_element_by_css_selector('h5.proTit').text)
    print('가격', li.find_element_by_css_selector('.proPrice').text.split('원')[0])
    print('='*100)

# body > div.container > div.searchSct > div > div.panelZone > div.recommService > div > ul > li