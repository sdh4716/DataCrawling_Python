from bs4 import BeautifulSoup
import requests
codes=['005930','036570']
prices = []
# document.querySelector("#chart_area > div.rate_info > div > p.no_today")

for code in codes:
    url = 'https://finance.naver.com/item/main.naver?code='+code
    res = requests.get(url)

    html = res.text
    soup = BeautifulSoup(res.content, 'html.parser')

    today= soup.select_one("#chart_area > div.rate_info > div > p.no_today")

    # print(today)
    price = today.select_one('.blind')
    prices.append(price.get_text())

print(prices)

# 불필요한 데이터를 제거하여 사용할 수 있는 데이터로 만드는것을 '데이터 전처리'라고 한다.