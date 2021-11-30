import numpy as np
import pandas as pd
import usecsv

#quest.csv 파일 읽기
# f = open('quest.csv','r')
# reader = csv.reader(f)

#읽은 파일을 배열 형태로 저장
# quest = np.array(usecsv.switchcsv(usecsv.opencsv('quest.csv')))
f = pd.read_csv('quest.csv', encoding='cp949')

print(quest)
 
print(quest>5)
quest[quest>5]
print(quest)