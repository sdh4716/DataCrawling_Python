print('Hello')
a=0
print(a)
print(type(a))
b="Hello World"
print(type(b))
print(b)
c="\'안녕하세요\'"
print(c)
print(b+c)
print(2*3)
print('2'*3)
print(c*3)
print(b[0])
print(b[-1])
d='안녕하세요'
print(d[1:3])
print(d[0:5:2]) #0부터 5까지 2씩 증가 
print(d[:]) #전체
##########
l = list() 
print(l, type(1))
lst = [1,2,3]
print(lst, type(lst))
l = [1,2,3,4,5,6,7,8,9,]
print(l[0])
print(len(l))
# l 리스트의 마지막 값 출력
print(l[-1])
# l의 0번째를 99로 수정
l[0] = 99
print(l)
l[1] = [1,2,3]
print(l)
l[2]='문자'
print(l)
l.append(999)
print(l)
l.remove(5)
print(l)

### tuple
t = tuple()
print(t, type(t)) #tuple은 ()로 표시
t1 = (1,2,3)
print(t1, type(t1))
print(t1[0], t1[0:2])
print(t1+t1)
# t1의 0번째를 5로 수정
# t1[0] = 5 tuple은 값을 변경할 수 없음 (오류)
print(t1)
### dict
d = dict()
print(d, type(d)) # dict는 중괄호로 나옴
d = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(d, type(d))
print(d['a'])
d['c'] = 33
print(d)
#print(d['d']) 오류발생
d1 = d.keys
print("d1 :", d1 )
d2 = d.items
print("d2 :", d2)
d3 = d.values
print("d3 :",d3)

### 조건문
a=2
if(a==1):
    print(1)
else:
    print("1아님")

#else if 가 아닌 elif
if(a==1):
    print(1)
elif(a==2):
    print(2)
else:
    print(3)

###반복문
for i in [1,2,3]:
    print(i)

for i in (1,2,3):
    print(i)
for i in "Hello":
    print(i)

num =5
while(num > 0):
    print(num)
    num -=1

# While문 사용

#10
#9
#8
#7
# --end--
num=10
while(num>0):
    if(num==6):
        print('--end--')
        break
    print(num, end=' ')
    num -=1

    for i in range(10):
        print(i)

#100까지의 수 중 7의 배수
sum=0
for i in range(100):
    if(i%7==0):
        sum+=i
        print(i, end=' ')
print("\nsum :", sum)

# * * *
# * * *
# * * *
for i in range(3):
    for j in range(3):
        print('*', end=' ')
        print('')    

a = input('숫자 입력')
print(a)
print(type(a))

a= int(a)
print(type(a))
a = float(a)
print(type(a))