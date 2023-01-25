#!/usr/bin/env python
# coding: utf-8

# In[6]:


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

df_movies = pd.read_csv('movies.csv') 
df_ratings = pd.read_csv('ratings.csv')
df_links = pd.read_csv('links.csv', dtype = object)
df_links.fillna(value=0, inplace=True)
df_tags = pd.read_csv('tags.csv')

header = {"accept-language": "es-ES"}

# def sacar_sinopsis(df_links, header):
#     results = []
#     for i, tmdbId in enumerate(df_links["tmdbId"]):
#         link = "https://www.themoviedb.org/movie/" + str(tmdbId)
#         r = requests.get(link, headers = header)
#         bs = BeautifulSoup(r.content, "html.parser")
#         try:
#             sinopsis = bs.p.get_text()
#             movie_id = df_links.at[i,"movieId"]
#             results.append([movie_id,tmdbId,sinopsis])
#         except:
#             results.append([tmdbId,"No se encontro sinopsis"])
#             continue
#         time.sleep(1)
#         print(f"{i+1}/{len(df_links)} completed")

#     df_sinopsis = pd.DataFrame(results,columns=['movieId','tmdbId','sinopsis'])
#     df_sinopsis.to_csv('sinopsis.csv', index=False)
#     return df_sinopsis
# df_sinopsis = sacar_sinopsis(df_links, header)

df_sinopsis = pd.read_csv('sinopsis.csv')

df_usuario = pd.read_csv('Usuario_0.csv')

def juntarMoviesSinopsis(df_movies, df_sinopsis, movieId, movies_sinopsis):
    # Unir los dataframes en función de la columna 'movieId'
    df_movies_sinopsis = pd.merge(df_movies, df_sinopsis, on='movieId')

    # Eliminar columna tmdbId
    df_movies_sinopsis = df_movies_sinopsis.drop('tmdbId', axis=1)
    
    # Guardar el resultado en un nuevo archivo CSV
    df_movies_sinopsis.to_csv('movies_sinopsis.csv', index=False)    
    return df_movies_sinopsis

#Comprobar que crea y elimina y guarda en un fichero csv
df_movies_sinopsis = juntarMoviesSinopsis(df_movies, df_sinopsis, 'movieId', 'movies_sinopsis.csv')

def get_sinopsis(title):
    # Leer el archivo CSV
    df_movies_sinopsis = pd.read_csv("movies_sinopsis.csv")

    # Buscar la sinopsis en el archivo CSV
    for i, row in df_movies_sinopsis.iterrows():
        if row["title"] == title:
            return row["sinopsis"]
    return "Sinopsis no encontrada"

def get_movie_info(buscar):
    # Leer el archivo CSV
    df = pd.read_csv("movies_sinopsis.csv")
    search_by = {"id": "movieId", "titulo": "title"}
    
    # Buscar la pelicula en el archivo CSV
    for i, row in df.iterrows():
        if row[search_by[buscar[0]]] == buscar[1]:
            return row[["movieId", "title", "genres","sinopsis"]]
    return "Pelicula no encontrada"

# class procesarTexto():
    
#     def tokenize(text):
        
#         return nltk.word_tokenize(text)
    
#     def clean_text(text):
#         # Eliminar números
#         text = re.sub(r'\d+', '', text)
#         # Eliminar signos de puntuación
#         text = re.sub(r'[^\w\s]', '', text)
#         # Convertir a minúsculas
#         text = text.lower()
#         return text

#     def remove_stopwords(text):
#         # Cargar lista de stopwords en español
#         stop_words = set(stopwords.words("spanish"))
#         # Tokenizar el texto
#         tokens = word_tokenize(text)
#         # Eliminar stopwords
#         filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
#         # Unir los tokens en una cadena de texto
#         filtered_text = ' '.join(filtered_tokens)
#         return filtered_text
    
#     def stem_text(text):
#         # Tokenizar el texto
#         tokens = word_tokenize(text)
#         # Crear un objeto stemmer
#         stemmer = SnowballStemmer("spanish")
#         # Aplicar stemming a cada token
#         stemmed_tokens = [stemmer.stem(token) for token in tokens]
#         # Unir los tokens en una cadena de texto
#         stemmed_text = ' '.join(stemmed_tokens)
#         return stemmed_text
    
#     def word_frequency(text):
#         # Tokenizar el texto
#         tokens = word_tokenize(text)
#         # Contar la frecuencia de cada token
#         freq = nltk.FreqDist(tokens)
#         # Devolver diccionario con la frecuencia de cada palabra
#         return dict(freq)
    
# def get_sinopsis(title):
# # Leer el archivo CSV
#     df = pd.read_csv("movies_sinopsis.csv")

#     # Buscar la sinopsis en el archivo CSV
#     for i, row in df.iterrows():
#         if row["title"] == title:
#             sinopsis = row["sinopsis"]
#             sinopsis = procesarTexto.clean_text(sinopsis)
#             sinopsis = procesarTexto.remove_stopwords(sinopsis)
#             sinopsis = procesarTexto.stem_text(sinopsis)
#             frequency = procesarTexto.word_frequency(sinopsis)
#             return sinopsis, frequency
#     return "Sinopsis no encontrada"

# # Ejemplo de uso
# title = "Toy Story (1995)"
# sinopsis, frequency = get_sinopsis(title)
# print(sinopsis)
# print(frequency) 

# def process_sinopsis(search_param):
#     movie_info = get_movie_info(search_param)
#     sinopsis = movie_info["sinopsis"]
#     sinopsis = clean_text(sinopsis)
#     sinopsis = remove_stopwords(sinopsis)
#     sinopsis = stem_text(sinopsis)
#     frequency = word_frequency(sinopsis)
#     return sinopsis, frequency

# search_param = ("id", 1)
# sinopsis, frequency = process_sinopsis(search_param)
# print(sinopsis)
# print(frequency)