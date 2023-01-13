#!/usr/bin/env python
# coding: utf-8

# DATA CLEANING WITH PYTHON

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


DeathbyCause = pd.read_csv(r"C:\Users\EliteBook\Downloads\10Alytics_Hackathon_Case Study\Final Datasets\1. annual-number-of-deaths-by-cause.csv")


# In[4]:


DeathbyCause


# In[5]:


DeathbyCause.info()


# In[6]:


DeathbyCause.isna().sum()


# In[7]:


DeathbyCause.dropna(axis=1, how='all', inplace=True) #dropping all null columns


# In[8]:


DeathbyCause.isna().sum()


# In[9]:


DeathbyCause.dropna(axis=0, inplace=True)
DeathbyCause  #dropping all null values


# In[10]:


DeathbyCause.isna().sum()


# No Null values our first data looks clean now

# In[11]:


DeathbyCause.to_excel('DeathbyCause.xlsx')


# In[12]:


#Now lets read the second dataset we will name as df2;Death by Age

df2=pd.read_csv(r"C:\Users\EliteBook\Downloads\10Alytics_Hackathon_Case Study\Final Datasets\2. number-of-deaths-by-age-group.csv")


# In[13]:


df2.isna().sum()


# In[14]:


#we will drop the code column
df2.drop(["Code"], axis=1, inplace=True)


# In[15]:


df2.info()


# In[25]:


df2.rename(columns={'Entity': 'Country'}, inplace=True)


# In[24]:


DeathbyCause


# Good to note that both datasets now have the same number of rows, now we will carry out a left merge the datasets using the entity and year as the primary key 

# In[26]:


Merge1= pd.merge(DeathbyCause, df2, on=["Country", "Year"])
Merge1


# In[29]:


#now let's read the third dataset Medical doctors Per10000 population as df4
df4 = pd.read_excel(r"C:\Users\EliteBook\Downloads\10Alytics_Hackathon_Case Study\Final Datasets\3. Medical Doctors Per 10000 population.xlsx")
df4


# In[30]:


df4.info()


# In[31]:


df4.rename(columns={'Location': 'Country', 'Period': 'Year'}, inplace=True) #renamed columns for ease of joining and consistency
df4


# In[32]:


df4.drop("Value", axis=1, inplace=True) #Blank cells is as a result of transformation, however the factvalue numeric and value are the same so i will drop it


# In[34]:


df5= pd.merge(Merge1, df4, on=["Country", "Year"]) #all 3 dataset merged
df5


# In[35]:


df6= pd.read_excel(r"C:\Users\EliteBook\Downloads\10Alytics_Hackathon_Case Study\Final Datasets\6. Current health expenditure (% of GDP).xlsx")


# In[36]:


df6.head()


# In[37]:


df6.isna().sum()


# In[38]:


df6.rename(columns={'Country Name': 'Country'}, inplace=True) #renamed columns for ease of joining and consistency
df6


# In[39]:


df7= pd.merge(df5, df6, on=["Country"])


# In[40]:


df7


# __df7: Is our dataset that contains 4 sets and i will be using this for the Exploratory data Analysis, while the word population dataset will be explored later on__

# <font size=4>__Exploratory Data Analysis__

# In[42]:


#Create a filter to only africa Countries
Africa = (df7["ParentLocation"] == 'Africa')
AfricaSet = df7[Africa].reset_index() 


# In[48]:


AfricaSet


# In[135]:


#df7[Africa].to_excel('df.xlsx') #importing to excel


# Data Visualization on powerbi is available on https://medium.com/@temenuoluwabusola/data-analysis-with-python-and-power-bi-27466f41fc0b

# In[ ]:




