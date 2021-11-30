import pandas as pd
#apt.csv 파일을 읽어 데이터 프레임형태로 출력
df = pd.read_csv('apt.csv',encoding='cp949')
print(type(df))
print(len(df))
print(df.head())
print(df.tail())
# 면적이 130 넘는 자료만 출력
print(df.면적>130)
print(df[df.면적>130])
print(df.지역)

#면적이 130 넘는 아파트의 가격 출력
print(df.가격[df.면적>130])
#면적이 130 넘고 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) & (df.가격<20000)])
#면적이 130 넘거나 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) | (df.가격<20000)])
# df.loc[원하는 행 조건, 원하는 열의 조건]
# 아파트와 가격만 
print(df.loc[:10,['아파트','가격']])
dfAsc = df.sort_values(by='가격',ascending=False)
print(dfAsc)
print(dfAsc.loc[:10,['아파트','가격']])
# 4억을 초과하는 가격으로 거래된 아파트, 가격만 출력
print(df.가격[df.가격>40000])
print(df.loc[:,['아파트','가격']][df.가격>40000])
df['단가'] = df.가격/df.면적
print(df.loc[:10, ('가격','면적','단가')])

#지역에 강릉이 들어간 자료만 출력
print(df[df.지역.str.find('강릉')>-1])
local_area=df[df.지역.str.find('강릉')>-1]
#강릉이 들어간 지역, 가격, 단가
print(local_area.loc[:10,('지역','가격','단가')])