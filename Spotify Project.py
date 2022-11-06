#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv(r'C:\Users\Aakasha\Desktop\Spotify\tracks.csv')


# In[4]:


#To get the first 5 rows:
df.head()


# 

# In[5]:


# for the first 10 rows
df.head(10)


# 

# In[6]:


#To check the null values
pd.isnull(df)


# In[7]:


#for the information of the dataframe
df.info()


# In[8]:


#To find 10 least popular songs
sort_df= df.sort_values('popularity',ascending = True).head(10)


# In[9]:


sort_df


# In[10]:



df.describe().transpose()


# In[11]:


#Most popular songs which are greater than 90 of TOP 10
#and I don't want to change the original dataFrame
most_popular=df.query('popularity>90', inplace=False).sort_values('popularity',ascending=False)
most_popular.head(10)


# In[12]:


#To change the Index column to release_date column
df.set_index('release_date', inplace=True)
df.index=pd.to_datetime(df.index)
df.head()
#Error,because it's already done


# In[13]:


#To know the 18th row at the artist
df[['artists']].iloc[18]


# In[14]:


#To convert runtime of the songs from MILLISECS to SECS
df['duration']=df['duration_ms'].apply(lambda x: round(x/1000))
df.drop('duration_ms',inplace=True, axis=1)
#The error came because, it's already done..


# In[15]:


df.head()


# In[16]:


#1st Visualiation
corr_df=df.drop(['key','mode','explicit'],axis=1).corr(method='pearson')
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt='.1g',vmin=-1,vmax=1,center=0,cmap='inferno',linewidths=1,linecolor='Black')
heatmap.set_title('Correlation Heatmap Between Variable')
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


# In[17]:


#To take the sample DataFrame
sample_df=df.sample(int(0.004*len(df)))


# In[18]:


print(len(sample_df))


# In[19]:


#Regrission plot b/w loudness and energy
plt.figure(figsize=(10,6))
sns.regplot(data=sample_df,y='loudness',x='energy',color='c').set(title='Loudness Vs Energy Correlation')


# In[20]:


plt.figure(figsize=(10,6))
sns.regplot(data=sample_df,y='popularity',x='acousticness',color='b').set(title='popularity Vs acoutiness Correlation')


# In[25]:


df['dates']=df.index.get_level_values('release_date')
df.dates=pd.to_datetime(df.dates)
years=df.dates.dt.year


# In[26]:


#Distrubution plot to visible the total no.of sums of each year since 1992
sns.displot(years,discrete=True, aspect=2, height=5, kind= 'hist').set(title='No of songs')


# In[ ]:


#pip install --user seaborn==0.11.0


# In[24]:



df.head()


# In[30]:


total_dr=df.duration
fig_dims=(18,7)
fig, ax = plt.subplots(figsize=fig_dims)
fig=sns.barplot(x=years,y=total_dr,ax=ax,errwidth=False).set(title='year Vs duration')
plt.xticks(rotation=90)


# In[32]:


total_dr=df.duration
sns.set_style(style='whitegrid')
fig_dims=(10,5)
fig,ax=plt.subplots(figsize=fig_dims)
fig=sns.lineplot(x=years,y=total_dr, ax=ax).set(title='Year Vs Duration')
plt.xticks(rotation=60)


# In[33]:


#2nd data analysis project using genres of the song
df_genre=pd.read_csv(r'C:\Users\Aakasha\Desktop\Spotify\SpotifyFeatures.csv')


# In[34]:


df_genre.head()


# In[38]:


#Duration of the songs at diff genres
plt.title('Duration of the Songs in Diff Genres')
sns.color_palette('rocket',as_cmap=True)
sns.barplot(y='genre',x='duration_ms',data=df_genre)
plt.xlabel('Duration in MilliSec')
plt.ylabel('Genres')


# In[39]:


#Top 5 genres by popularity
sns.set_style(style='darkgrid')
plt.figure(figsize=(10,5))
famous=df_genre.sort_values('popularity',ascending=False).head(10)
sns.barplot(y='genre',x='popularity',data=famous).set(title='Top 5 Genres by popularity')


# In[ ]:




