#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

red_df = pd.read_csv('winequality-red.csv',sep=';',header=0, engine='python')
white_df = pd.read_csv('winequality-white.csv',sep=';',header=0, engine='python')

red_df.to_csv('winequality-red2.csv',index=False)
white_df.to_csv('winequality-white2.csv',index=False)


# In[5]:


red_df.describe()


# In[6]:


red_df.shape


# In[8]:


white_df.shape


# In[9]:


red_df.insert(0,column='type',value='red')


# In[10]:


red_df.shape


# In[11]:


red_df.head()


# In[15]:


white_df.insert(0,column='type',value='white')
white_df.shape


# In[14]:


white_df.head()


# In[16]:


wine = pd.concat([red_df, white_df])


# In[17]:


wine.shape


# In[19]:


wine.head() # 상위 5개의 데이터


# In[20]:


wine.tail() # 하위 5개의 데이터


# In[21]:


wine.to_csv('wine.csv',index=False)


# In[24]:


wine.columns = wine.columns.str.replace(' ','_') #공백을 _로 바꾼다


# In[25]:


wine.head()


# In[26]:


wine.describe()


# In[29]:


sorted(wine.quality.unique())


# In[30]:


wine.quality.value_counts() #빈도 수 


# In[31]:


wine.groupby('type')['quality'].describe() #std:표준편차 25분위,50분위, 75분위


# In[32]:


wine.groupby('type')['quality'].mean()


# In[33]:


wine.groupby('type')['quality'].std()


# In[34]:


wine.groupby('type')['quality'].agg(['mean','std'])


# In[35]:


from scipy import stats #, t-검정(그룹 비교)
from statsmodels.formula.api import ols, glm #회귀분석 statsmodel


# In[37]:


red_wine_quality=wine.loc[wine['type']=='red','quality']
white_wine_quality=wine.loc[wine['type']=='white','quality']


# In[38]:


stats.ttest_ind(red_wine_quality,white_wine_quality,equal_var=False)


# In[39]:


wine.head()


# In[50]:


#quality에 대한 독립변수
Rformula='quality~fixed_acidity + volatile_acidity + citric_acid + residual_sugar+ chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates +alcohol'
#fit() 함수로 훈련시킴
regression_result = ols(Rformula,data=wine).fit()
          


# In[41]:


regression_result.summary()


# In[42]:


sample1 = wine[wine.columns.difference(['quality','type'])]
sample1 = sample1[0:5][:]
sample1


# In[48]:


# 훈련시킨 결과로 예측
sample1_predict = regression_result.predict(sample1)
sample1_predict


# In[45]:


wine[0:5]['quality']


# In[51]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('dark')
sns.histplot(red_wine_quality, kde=True, color='red', label='red wine')
sns.histplot(white_wine_quality, kde=True, label='white wine')
plt.title('Quality of Wine Type')
plt.legend()
plt.show()

