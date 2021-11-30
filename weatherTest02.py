import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# weather.csv 읽어 출력하기
df=pd.read_csv('weather.csv',index_col='point', encoding='euc-kr')
print(df)
city_df=df.loc[['서울','인천','대전','대구','광주','부산','울산']]
print(city_df)

#그래프 그리기
#한글 처리
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/Hancom Gothic Bold.ttf').get_name()
mpl.rc('font', family=font_name)

ax = city_df.plot(kind='bar', title='날씨', figsize=(12,7), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도',fontsize=12)
ax.legend(['기온','습도'],fontsize=12)
plt.show()