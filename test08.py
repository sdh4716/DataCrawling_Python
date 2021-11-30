import usecsv

total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switchcsv(total)

print(newPop[:4])
new = [['구','한국인','외국인','외국인비율(%)']]

for i in newPop:
    foreign = 0
    try:
         foreign = round(i[2]/(i[1]+i[2])*100,1)
        # print(i[0],foreign)
         if foreign > 5:
          # print(i[0],foreign)
          new.append([i[0],i[1],i[2],foreign])
    except:
            pass
print(new)