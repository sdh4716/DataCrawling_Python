import csv, re

def opencsv(filename):
    f = open(filename,'r')
    reader = csv.reader(f)
    output =[]
    for i in reader:
        output.append(i)
    return output

total = opencsv('popSeoul.csv')

for i in total[:5]:
    print(i)

# j = '1,468,246'
# print(float(re.sub(',','',j)))


test = [1,2,3,4,5]
print(test.index(5)) # index 위치(index를 알고자 할때)

for i in total[:5]:
    for j in i:
        try:
          i[i.index(j)] = float(re.sub(',','',j))
        except:
            pass
        
print(total[:5])

# new = [['구','한국인','외국인','외국인비율(%)']]
# for i in total[:5]:
#     foreign = 0

#     foreign = round(i[2]/(i[1]+i[2])*100,1)
#     print(i[0], foreign)