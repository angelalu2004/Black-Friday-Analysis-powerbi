#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[6]:


train = pd.read_csv('/Users/SONY/Desktop/data_analysis/black_friday/train.csv')


# In[7]:


train.head()


# In[8]:


train.info()


# In[9]:


train.shape[0]


# In[10]:


train.Product_Category_2.fillna(0,inplace = True)


# In[11]:


train.Product_Category_3.fillna(0, inplace = True)


# In[44]:


train.info()


# In[45]:


train.head()


# In[48]:


train.duplicated().sum()


# In[49]:


train.tail()


# In[16]:


train1 = train.copy()


# In[17]:


train1.describe()


# In[19]:


train1.to_csv('train1.csv')


# In[ ]:




