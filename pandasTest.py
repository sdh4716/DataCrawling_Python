import pandas as pd

data = {
    'name' : ['Mark','Jane','aaa','rr'],
    'age' : [33,44,55,11],
    'score': [91.2, 88.5, 55.6, 88.9]
}

df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.sum())
print(df.mean())
# print(df.age)
print(df['age'])