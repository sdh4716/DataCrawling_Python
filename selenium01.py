from selenium import webdriver as wd

# \는 무조건 \\ 두번
path ='C:\\ChromeDriver\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = wd.Chrome(path, options=options)
driver.get('https://naver.com')
# print(driver)
#복수개가 필요할때는 find_elements
driver.find_element_by_id('query').send_keys('파이썬') #send_keys:키보드 입력
driver.find_element_by_id('search_btn').click() #click 마우스 클릭
