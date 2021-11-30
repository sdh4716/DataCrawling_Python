from bs4 import BeautifulSoup
import re
html ="""
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="https://example.com/aaa">aaa</li>
    </ul>
"""

soup = BeautifulSoup(html,"html.parser")
li = soup.find_all(href=re.compile(r"^https://"))
print(li)
for e in li:
    print(e.attrs['href'])