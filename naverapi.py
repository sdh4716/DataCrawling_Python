import urllib.request
import datetime
import json

client_Id = "TAhhJVqGWurablNBGMcf"
client_Secret = "7IZfy4tY8d"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_Id)
request.add_header("X-Naver-Client-Secret",client_Secret)

def getRequestUrl(url) :
    req = urllib.request.Request(url)

    req.add_header("X-Naver-Client-Id", client_Id)    
    req.add_header("X-Naver-Client-Secret", client_Secret)  

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
             print("[%s] Url Request Success " % datetime.datetime.now())
             return response.read().decode('utf-8')


    except Exception as e :
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearch(node, srcText, start, display) :
    base = "https://openapi.naver.com/v1/search"
    node = "/news.json"
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(srcText),start, display)
    url = base+ node + parameters
    print(url)
    responseDecode = getRequestUrl(url)

    if (responseDecode == None) :
        return None
    else :
        return json.loads(responseDecode) # load() json문자열을 객체로 바꿔준다
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = post['pubDate']

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description,
                       'org_link':org_link, 'link':link, 'pDate':pDate})

node = 'news'
srcText ='선거'
cnt = 0
jsonResult = []

jsonResponse = getNaverSearch(node,srcText,1,100)
total = jsonResponse['total']

while((jsonResponse != None) and (jsonResponse['display']!=0)):
    for post in jsonResponse['items']:
        cnt += 1
        getPostData(post, jsonResult, cnt)

    start = jsonResponse['start'] + jsonResponse['display']
    jsonResponse = getNaverSearch(node,srcText,start,100)

print('전체 검색 : %d 건' %total)

with open('%s_naver_%s.json' %(srcText, node), 'w' , encoding='utf-8') as outfile :
    jsonFile = json.dumps(jsonResult, indent = 4, sort_keys=True, ensure_ascii=True)
    outfile.write(jsonFile)

print("가져온 데이터 : %d 건 " %(cnt))
print("%s_naver_%s.json.SAVED" %(srcText, node))