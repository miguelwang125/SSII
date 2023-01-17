#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt 
import requests

df_movies = pd.read_csv('movies.csv') 

df_ratings = pd.read_csv('ratings.csv')

df_links = pd.read_csv('links.csv', dtype = object)

df_tags = pd.read_csv('tags.csv')

df_movies

df_ratings

df_links

df_tags

link = "https://www.themoviedb.org/movie/" + df_links["tmdbId"][0]

header = {"accept-language": "es-ES"}

for i in df_links["tmdbId"]:
    link = "https://www.themoviedb.org/movie/" + i
    r = requests.get(link, headers = header)
    bs = BeautifulSoup(r.content, "html.parser")
    print(bs.p.get_text())

r = requests.get(link, headers = header)

bs = BeautifulSoup(r.content, "html.parser")

print (bs.prettify)

print(bs.p.get_text())

# Leer el archivo CSV
with open('links.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]
    
# Realizar una búsqueda en la web para cada elemento de la lista
for imdbId in data:
    url = "https://www.imdb.com/title/tt"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', class_='result')
    for result in results:
        print(result.text)

# Recorrer las filas de una columna específica
for valor in df['imdbId']:
    # Hacer una solicitud a una página web
    respuesta = requests.get("https://www.imdb.com")

    # Buscar el valor de la columna en la página
    if valor in respuesta.text:
        print(valor + " encontrado en la página")
    else:
        print(valor + " no encontrado en la página")