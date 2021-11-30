
import pymysql
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import matplotlib

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='bigdb',charset='utf8', use_unicode=True)
select_data = "select * from forecast where city='부산' "

font_path = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font',family = font_name)

cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()

high = []
low = []
xdata=[]

for row in result:
    high.append(row[5])
    low.append(row[4])
    xdata.append(row[2].split('-')[2])

# print(high)
plt.figure(figsize=(10,6))  #그래프 크기
plt.plot(xdata,low, label='최저기온')
plt.plot(xdata,high, label='최고기온')

plt.legend()
plt.show()

#########
select_data1 = "select wf, count(*) from forecast where city='부산'  group by wf"
cur.execute(select_data1)
result1 = cur.fetchall()
wfData=[]
wfDataCount =[]
for row in result1:
    wfData.append(row[0])
    wfDataCount.append(row[1])

plt.bar(wfData,wfDataCount)
plt.show()    


plt.pie(wfDataCount,labels=wfData,autopct='%.1f%%')
plt.show()