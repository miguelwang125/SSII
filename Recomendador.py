#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt 

from bs4 import BeautifulSoup
import requests
import time


# In[2]:


df_movies = pd.read_csv('movies.csv') 


# In[3]:


df_ratings = pd.read_csv('ratings.csv')


# In[4]:


df_links = pd.read_csv('links.csv', dtype = object)
df_links.fillna(value=0, inplace=True)


# In[5]:


df_tags = pd.read_csv('tags.csv')


# In[ ]:





# In[ ]:


df_movies


# In[ ]:


df_ratings


# In[ ]:


df_links


# In[ ]:


df_tags


# In[ ]:





# In[6]:


header = {"accept-language": "es-ES"}


# In[ ]:


r = requests.get(link, headers = header)


# In[ ]:





# In[7]:


results = []
for i, tmdbId in enumerate(df_links["tmdbId"]):
    link = "https://www.themoviedb.org/movie/" + str(tmdbId)
    r = requests.get(link, headers = header)
    bs = BeautifulSoup(r.content, "html.parser")
    try:
        sinopsis = bs.p.get_text()
        results.append([tmdbId,sinopsis])
    except:
        results.append([tmdbId,"No se encontro sinopsis"])
        continue
    time.sleep(1)
    print(f"{i+1}/{len(df_links)} completed")

df = pd.DataFrame(results,columns=['tmdbId','sinopsis'])
df.to_csv('sinopsis.csv', index=False)


# In[ ]:





# In[ ]:


link = "https://www.themoviedb.org/movie/" + df_links["tmdbId"][0]


# In[ ]:


bs = BeautifulSoup(r.content, "html.parser")


# In[ ]:


print (bs.prettify)


# In[ ]:


print(bs.p.get_text())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




