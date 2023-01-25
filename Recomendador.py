#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt 

from bs4 import BeautifulSoup
import requests
import time
import re

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


# In[ ]:





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


# In[32]:


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
df_sinopsis = sacar_sinopsis(df_links, header)


# In[ ]:





# In[45]:


df_sinopsis = pd.read_csv('sinopsis.csv')


# In[46]:


df_usuario = pd.read_csv('Usuario_0.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[47]:


def juntarMoviesSinopsis(df_movies, df_sinopsis, movieId, movies_sinopsis):
    # Unir los dataframes en función de la columna 'movieId'
    df_movies_sinopsis = pd.merge(df_movies, df_sinopsis, on='movieId')

    # Eliminar columna tmdbId
    df_movies_sinopsis = df_movies_sinopsis.drop('tmdbId', axis=1)
    
    # Guardar el resultado en un nuevo archivo CSV
    df_movies_sinopsis.to_csv('movies_sinopsis.csv', index=False)    
    return df_movies_sinopsis


# In[48]:


#Comprobar que crea y elimina y guarda en un fichero csv
df_movies_sinopsis = juntarMoviesSinopsis(df_movies, df_sinopsis, 'movieId', 'movies_sinopsis.csv')
print(df_movies_sinopsis)


# In[ ]:





# In[49]:


def get_sinopsis(movie_id):
    # Leer el archivo CSV
    df = pd.read_csv("movies_sinopsis.csv")

    # Buscar la sinopsis en el archivo CSV
    for i, row in df.iterrows():
        if row["movieId"] == movie_id:
            return row["sinopsis"]
    return "Sinopsis no encontrada"

# Ejemplo de uso
movie_id = 2
sinopsis = get_sinopsis(movie_id)
print(sinopsis)


# In[52]:


def get_sinopsis(title):
    # Leer el archivo CSV
    df = pd.read_csv("movies_sinopsis.csv")

    # Buscar la sinopsis en el archivo CSV
    for i, row in df.iterrows():
        if row["title"] == title:
            return row["sinopsis"]
    return "Sinopsis no encontrada"

# Ejemplo de uso
title = "Toy Story (1995)"
sinopsis = get_sinopsis(title)
print(sinopsis)


# In[57]:


def get_movie_info(movieId, title):
    # Leer el archivo CSV
    df = pd.read_csv("movies_sinopsis.csv")

    # Buscar la pelicula en el archivo CSV
    for i, row in df.iterrows():
        if row[title] == movieId:
            return row[["movieId", "titulo", "genero","sinopsis"]]
    return "Pelicula no encontrada"

# Ejemplo de uso
movieId = 1
title = "Toy Story (1995)"
movie_info = get_movie_info(movieId, title)
print(movie_info)


# In[62]:


def get_movie_info(buscar):
    # Leer el archivo CSV
    df = pd.read_csv("movies_sinopsis.csv")
    search_by = {"id": "movieId", "titulo": "title"}
    
    # Buscar la pelicula en el archivo CSV
    for i, row in df.iterrows():
        if row[search_by[buscar[0]]] == buscar[1]:
            return row[["movieId", "title", "genres","sinopsis"]]
    return "Pelicula no encontrada"

# Ejemplo de uso mediante id y titulo
buscar = ("id", 1)
buscar = ("titulo", "Toy Story (1995)")
movie_info = get_movie_info(buscar)
print(movie_info)


# In[ ]:





# In[23]:


df_movies = pd.read_csv('movies.csv')
df_usuario = pd.read_csv('Usuario_0.csv')


# In[24]:


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


# In[25]:


#Comprobar que crea y elimina y guarda en un fichero csv
dfPNVU0 = sacarPelisNoVistasPorU0(df_movies, df_usuario, 'movieId', 'PNVU0.csv')
print(dfPNVU0)


# In[26]:


dfPNVU0


# In[ ]:





# In[ ]:


# Tokenizar
tokens = word_tokenize(sinopsis)

# Eliminar stopwords
stop_words = set(stopwords.words("spanish"))
tokens = [token for token in tokens if token.lower() not in stop_words]

# Stemming
stemmer = SnowballStemmer("spanish")
tokens = [stemmer.stem(token) for token in tokens]

# Frecuencia de palabras
freq = nltk.FreqDist(tokens)
print(freq.most_common(10))


# In[54]:


class procesarTexto():
    
    def tokenize(text):
        
        return nltk.word_tokenize(text)
    
    def clean_text(text):
        # Eliminar números
        text = re.sub(r'\d+', '', text)
        # Eliminar signos de puntuación
        text = re.sub(r'[^\w\s]', '', text)
        # Convertir a minúsculas
        text = text.lower()
        return text

    def remove_stopwords(text):
        # Cargar lista de stopwords en español
        stop_words = set(stopwords.words("spanish"))
        # Tokenizar el texto
        tokens = word_tokenize(text)
        # Eliminar stopwords
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
        # Unir los tokens en una cadena de texto
        filtered_text = ' '.join(filtered_tokens)
        return filtered_text
    
    def stem_text(text):
        # Tokenizar el texto
        tokens = word_tokenize(text)
        # Crear un objeto stemmer
        stemmer = SnowballStemmer("spanish")
        # Aplicar stemming a cada token
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        # Unir los tokens en una cadena de texto
        stemmed_text = ' '.join(stemmed_tokens)
        return stemmed_text
    
    def word_frequency(text):
        # Tokenizar el texto
        tokens = word_tokenize(text)
        # Contar la frecuencia de cada token
        freq = nltk.FreqDist(tokens)
        # Devolver diccionario con la frecuencia de cada palabra
        return dict(freq)
    
    


# In[ ]:


def get_sinopsis(title):
    # Leer el archivo CSV
    df = pd.read_csv("movies_sinopsis.csv")

    # Buscar la sinopsis en el archivo CSV
    for i, row in df.iterrows():
        if row["title"] == title:
            sinopsis = row["sinopsis"]
            sinopsis = clean_text(sinopsis)
            sinopsis = remove_stopwords(sinopsis)
            sinopsis = stem_text(sinopsis)
            frequency = word_frequency(sinopsis)
            return sinopsis, frequency
    return "Sinopsis no encontrada"

# Ejemplo de uso
title = "Toy Story (1995)"
sinopsis, frequency = get_sinopsis(title)
print(sinopsis)
print(frequency)

