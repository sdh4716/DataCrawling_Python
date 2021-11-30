import requests

r = requests.get("http://api.aoikujira.com/time/get.php")

# print(r)
text = r.text # 텍스트 형식으로 데이터 추출
print(text)
bin = r.content #바이너리 형식으로 데이터 추출
print(bin)
