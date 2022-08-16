#!/usr/bin/env python
# coding: utf-8

# # numpy

# In[5]:


#create 6*6 2d array and le 1 and 0 be placed alternatively accross the diagonals
import numpy as np
a = np.zeros((6,6),dtype = int)
a[1::2,::2] = 1 #a[x-axis,y-axis] = 1 i.e a[x--1st row:until last:2step ,y--0th row:until 2nd last:step of 2]
a[::2,1::2] = 1 # a[0th row:until 2nd last:step of 2, ]
a


# In[15]:


#find total no,s and locations of missing values in array
z = np.random.rand(10,10)
z[np.random.randint(10,size = 5), np.random.randint(10,size = 5)] = np.nan
print("\nprint the total no. of missind values : ", np.isnan(z).sum())
print("\nprint the position/indexes of missinf values : ", np.argwhere(np.isnan(z)))
print(np.where(np.isnan(z)))


# In[16]:


#using matplotlib try to plot a sin graph
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()


# # pandas

# In[18]:


import pandas as pd
print(pd.__version__)


# In[26]:


arr = [1,3,4,8,2,9]
s = pd.Series(arr)
print(s)
order = ['a','b','c','d','e','f']
s = pd.Series(arr, index = order) #the order of index and the array should match
print(s)
s.index = [1,2,3,4,5,6] #modifying index
print(s)


# In[24]:


n = np.random.randn(6)
s1 = pd.Series(n , index = order)
print(s1)


# In[25]:


d = {'a':1 , 'b':2 , 'c':3 , 'd':4}
s2 = pd.Series(d)
print(s2)


# In[33]:


s3 = s.append(s1)
s3.drop('e')


# In[36]:


a = [1,2,3,4,5,6]
b = [6,7,8,9,2]
s4 = pd.Series(a)
s5 = pd.Series(b)
print(s4.add(s5))
print(s4.sub(s5))
print(s4.mul(s5))
print(s4.div(s5))
print(s4.median())
print(s4.max())
print(s4.min())


# In[54]:


# dataframes
dates = pd.date_range("today",periods = 6)
print(dates)
num_arr = np.random.randn(6,4)
print(num_arr)
columns = ['a','b','c','d']
df1 = pd.DataFrame(num_arr, index=dates, columns = columns)
print(df1.T)


# In[55]:


print(df1.dtypes)
print(df1.head(2))
print(df1.tail(2))
print(df1.describe())
# print(df1.T)
df1.sort_values(by='a')


# In[57]:


dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
df = pd.DataFrame(dict)
df


# In[69]:


# dataframe file operations
df.to_csv('dict.csv')
df_dict = pd.read_csv('dict.csv')
df_dict.head(2)


# In[70]:


df.to_excel('dict.xlsx',sheet_name = 'sheet')
df_dict2=pd.read_excel('dict.xlsx','sheet',index_col=None,na_values=['NA'])
df_dict2


# In[74]:


# visulization in pandas
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
ts = pd.Series(np.random.randn(50), index=pd.date_range('today',periods=50))
ts = ts.cumsum()
ts.plot()


# In[76]:


df = pd.DataFrame(np.random.randn(50,4), index=ts.index, columns = ['A','B','C','D'])
df = df.cumsum()
df.plot()


# In[77]:


#remove repeated data using pandas
df = pd.DataFrame({'A':[1,2,2,3,4,4,4,5,5,6,7,7,8]})
df.loc[df['A'].shift()!=df['A']]


# In[ ]:




