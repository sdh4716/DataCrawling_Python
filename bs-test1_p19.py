from bs4 import BeautifulSoup

html ="""
    <html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""

soup = BeautifulSoup(html,'html.parser')
print(soup)
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print("h1 =", h1.string)
print("p1 =", p1.string)
print("p2 =", p2.string)

html2 ="""
    <html><body>
    <h1 id='title'>스크레이핑이란?</h1>
    <p id='body'>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""
soup = BeautifulSoup(html2,'html.parser')
title = soup.find(id='title')
print('#title = ', title.string)
body = soup.find(id='body')
print('#body = ', body.string)