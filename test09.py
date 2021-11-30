import csv
import re

f = open('popSeoul.csv','r')
reader = csv.reader(f)
print(reader)
output =[]

for i in reader:
    for j in i:
        try:
            if re.search('\d',j):
                i[i.index(j)] = float(re.sub(',','',j))
                output.append(i)
        except:
            output.append(i)
# print(output)

for i in output:
    foreign = 0
    try:
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        if foreign > 3:
            print(i[0],i[1],i[2],foreign)
    except:
        pass
