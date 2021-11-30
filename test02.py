def seperate():
    a = input("수 입력")
    if a%2==0:
        print("짝수")
    else:
        print('홀수')

def addReturn(a,b):
    return a+b

seperate()
print(addReturn(3,5))
