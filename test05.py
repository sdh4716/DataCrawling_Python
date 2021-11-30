import requests

URL = 'http://www.naver.com'
response = requests.get(URL)
html_data = response.text
print(html_data)

print(html_data.find('<div class=service_area>'))
print(html_data[100:150])