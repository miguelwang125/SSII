#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt 
import requests

from bs4 import BeautifulSoup
import requests
import time


# In[ ]:





# In[2]:


df_movies = pd.read_csv('movies.csv') 

df_ratings = pd.read_csv('ratings.csv')

df_links = pd.read_csv('links.csv', dtype = object)
df_links.fillna(value=0, inplace=True)

df_tags = pd.read_csv('tags.csv')


# In[ ]:





# In[ ]:





# In[22]:


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


def sacar_sinopsis(df_links, header):
    results = []
    for i, tmdbId in enumerate(df_links["tmdbId"]):
        link = "https://www.themoviedb.org/movie/" + str(tmdbId)
        r = requests.get(link, headers = header)
        bs = BeautifulSoup(r.content, "html.parser")
        try:
            sinopsis = bs.p.get_text()
            movie_id = df_links.at[i,"movieId"]
            results.append([movie_id,tmdbId,sinopsis])
        except:
            results.append([tmdbId,"No se encontro sinopsis"])
            continue
        time.sleep(1)
        print(f"{i+1}/{len(df_links)} completed")

    df_sinopsis = pd.DataFrame(results,columns=['movieId','tmdbId','sinopsis'])
    df_sinopsis.to_csv('sinopsis.csv', index=False)
    return df_sinopsis


# In[ ]:


df_sinopsis = sacar_sinopsis(df_links, header)


# In[ ]:





# In[7]:


link = "https://www.themoviedb.org/movie/" + df_links["tmdbId"][0]


# In[8]:


r = requests.get(link, headers = header)


# In[9]:


bs = BeautifulSoup(r.content, "html.parser")


# In[10]:


print (bs.prettify)


# In[11]:


print(bs.p.get_text())


# In[ ]:





# In[ ]:





# In[12]:


df_sinopsis = pd.read_csv('sinopsis.csv')


# In[13]:


df_usuario = pd.read_csv('Usuario_0.csv')


# In[ ]:





# In[14]:


def juntarMoviesSinopsis(df_movies, df_sinopsis, movieId, movies_sinopsis):
    # Unir los dataframes en función de la columna 'movieId'
    df_movies_sinopsis = pd.merge(df_movies, df_sinopsis, on='movieId')

    # Eliminar columna tmdbId
    df_movies_sinopsis = df_movies_sinopsis.drop('tmdbId', axis=1)
    
    # Guardar el resultado en un nuevo archivo CSV
    df_movies_sinopsis.to_csv('movies_sinopsis.csv', index=False)    
    return df_movies_sinopsis


# In[15]:


#Comprobar que crea y elimina y guarda en un fichero csv
df_movies_sinopsis = juntarMoviesSinopsis(df_movies, df_sinopsis, 'movieId', 'movies_sinopsis.csv')
print(df_movies_sinopsis)


# In[51]:


df_movies = pd.read_csv('movies.csv')
df_usuario = pd.read_csv('Usuario_0.csv')


# In[54]:


def sacarPelisNoVistasPorU0(df_movies, df_usuario, movieId, PNVU0):
    # Unir los dataframes en función de la columna 'movieId'
    merged_df = pd.merge(df_movies, df_usuario, on='movieId', how='outer', indicator=True)
    
    dfPNVU0 = merged_df[merged_df['_merge'].isin(['left_only', 'right_only'])]
    # Eliminar columna tmdbId
    dfPNVU0.drop(columns='_merge', inplace=True)
    dfPNVU0.drop('title_y', axis=1, inplace=True)
    dfPNVU0 = dfPNVU0.rename(columns={'title_x': 'title'})
    
    # Guardar el resultado en un nuevo archivo CSV
    dfPNVU0.to_csv("PNVU0.csv", index=False)    
    return dfPNVU0


# In[55]:


#Comprobar que crea y elimina y guarda en un fichero csv
dfPNVU0 = sacarPelisNoVistasPorU0(df_movies, df_usuario, 'movieId', 'PNVU0.csv')
print(dfPNVU0)


# In[56]:


dfPNVU0


# In[ ]:





# In[ ]:





# In[ ]:




