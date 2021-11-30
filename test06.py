import re, codecs
f = codecs.open('friends101.txt','r',encoding='utf-8')
script101 = f.read()

print(script101[:100])

Line = re.findall(r'Monica:.+',script101)
print(Line[:3])
print(type(Line))

char = re.compile(r'[A-z][a-z]+:')
print(re.findall(char,script101))

a = [1,2,3,4,5,2,2]
print(set(a))
print(set(re.findall(char,script101)))
y=set(re.findall(char,script101))
print(type(y))
z = list(y)
character = []

for i in z:
    character += [i[:-1]]

print(character)

ch = 'Scene:'
ch = re.sub(':','',ch)
print(ch)

#================
txt = re.findall(r'\([A-za-z].+[a-z|\.]\)',script101)[:6]
print(txt)
print(type(txt))
#================
a = '제 이메일 주소는 greate@naver.com 오늘은 today@naver.com'
a +=  '내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'

mail = re.findall(r'[a-z]+@[a-z.]+',a)
print(mail)

words=['apple','cat','brave','drama','aside','blow','coat','above']
for i in words:
    m = re.search(r'a[a-z]+',i)
    if m:
        print(m.group())
print('')
for i in words:
    #m = re.match(r'a[a-z]+',i)
    m=re.match(r'a\D+',i) #d (숫자) D(숫자 아닌)
    if m:
        print(m.group())

# f = open('monica.txt','w',encoding='utf-8')
# monica = ''
# for i in Line:
#     monica += i
# f.write(monica)