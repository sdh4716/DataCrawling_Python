#p41
#1~10까지의 합 출력
sum=0
for i in range(1,11):
 sum += i
 print(sum)

#p44 구구단 출력(2단~9단)
print("====구구단====")
for i in range(2,10):
    print(i,"단")
    for j in range(1,10):
        gugu = i*j
        print(i,"*",j,"=",gugu)
#p75 문자열에서 무작위로 5개 문자 추출하여 새로운 변수 pw에 하나씩 병합
import random
pw = str()
chars = '한글우수'
for _ in range(5):
    pw = pw + random.choice(chars) #random에서 무작위로 하나 뽑음
print(pw)

#p83 animal 리스트에서 새가 저장되어 있는 위치(인덱스만 저장)
bird_pos = []
animals = ['새','코끼리','강아지','새','강아지','새']
for i, animal in enumerate(animals):
    print('i :', i)
    print('animal :', animal)
    if(animal=='새'):
        bird_pos.append(i)
print(bird_pos)

#p84 mylist에서 짝수만 출력
mylist = [3,5,4,9,2,8,2,1]
new_list = [i for i in mylist if (i%2)==0]
print(new_list)
#p84 19세 이상인 사람만 추출하여 리스트 adult에 저장
people = [31, 53, 41, 19, 15, 18, 21, 13]
adult = [i for i in people if(i>=19)]

print(adult)
#90 항목이 2인것만 추출하여 newlist생성
mylist= [[1,2],[3,4,5],[6,7]]
newlist = [x for x in mylist if len(x)==2]
print(newlist)