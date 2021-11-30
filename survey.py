import pandas as pd

#head()출력
df = pd.read_csv('survey.csv', encoding='cp949')
print(df.head())
print(df.mean())
print("수입평균 : ",df.income.mean())
print("수입합계 :",df.income.sum())
print("수입중앙값 :",df.income.median())
print("===describe()=====")
print(df.describe())
print(df.sex.value_counts())