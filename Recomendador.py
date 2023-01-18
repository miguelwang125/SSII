#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt 

<<<<<<< HEAD
from bs4 import BeautifulSoup
import requests
import time

=======
>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6

# In[2]:


df_movies = pd.read_csv('movies.csv') 


# In[3]:


df_ratings = pd.read_csv('ratings.csv')


# In[4]:


df_links = pd.read_csv('links.csv', dtype = object)
<<<<<<< HEAD
df_links.fillna(value=0, inplace=True)
=======
>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6


# In[5]:


df_tags = pd.read_csv('tags.csv')


# In[ ]:





<<<<<<< HEAD
# In[ ]:
=======
# In[8]:
>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6


df_movies


<<<<<<< HEAD
# In[ ]:
=======
# In[6]:
>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6


df_ratings


# In[ ]:


<<<<<<< HEAD
df_links


=======
df_ratings


# In[10]:


df_links


# In[15]:





# In[48]:





>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6
# In[ ]:


df_tags


# In[ ]:


<<<<<<< HEAD



# In[6]:


header = {"accept-language": "es-ES"}


# In[ ]:


def cargarSinopsis():
    for i in df_links["tmdbId"]:
        link = "https://www.themoviedb.org/movie/" + i
        r = requests.get(link, headers = header)
        bs = BeautifulSoup(r.content, "html.parser")
        print(bs.p.get_text())
        


# In[ ]:


print(cargarSinopsis())


# In[ ]:





# In[ ]:


for i in df_links["tmdbId"]:
    print(i) 
    link = "https://www.themoviedb.org/movie/" + str(i)
    r = requests.get(link, headers = header)
    bs = BeautifulSoup(r.content, "html.parser")
    try:
        sinopsis = bs.p.get_text()
        print(sinopsis)
    except:
        print("No se encontro sinopsis para el tmdbId: ",i)
        continue
    time.sleep(1)


# In[ ]:





# In[ ]:





# In[ ]:


results = []
for i in df_links["tmdbId"]:
    link = "https://www.themoviedb.org/movie/" + str(i)
    r = requests.get(link, headers = header)
    bs = BeautifulSoup(r.content, "html.parser")
    try:
        sinopsis = bs.p.get_text()
        results.append([i,sinopsis])
    except:
        results.append([i,"No se encontro sinopsis"])
        continue
    time.sleep(1)
    
df = pd.DataFrame(results,columns=['tmdbId','sinopsis'])
df.to_csv('sinopsis.csv', index=False)


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





# In[ ]:





# In[ ]:


=======
>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6
link = "https://www.themoviedb.org/movie/" + df_links["tmdbId"][0]


# In[ ]:


<<<<<<< HEAD
bs = BeautifulSoup(r.content, "html.parser")
=======
header = {"accept-language": "es-ES"}

for i in df_links["tmdbId"]:
    link = "https://www.themoviedb.org/movie/" + i
    r = requests.get(link, headers = header)
    bs = BeautifulSoup(r.content, "html.parser")
    print(bs.p.get_text())


# In[14]:





# In[41]:


header = {"accept-language": "es-ES"}


# In[42]:


r = requests.get(link, headers = header)
>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6


# In[ ]:


<<<<<<< HEAD
print (bs.prettify)


# In[ ]:
=======



# In[43]:


bs = BeautifulSoup(r.content, "html.parser")


# In[44]:


print (bs.prettify)


# In[46]:
>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6


print(bs.p.get_text())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


<<<<<<< HEAD



# In[ ]:





# In[ ]:



=======
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


# In[ ]:





# In[ ]:


import pandas as pd
import requests

# Leer el archivo CSV usando Pandas
df = pd.read_csv("links.csv")

# Recorrer las filas de una columna específica
for valor in df['imdbId']:
    # Hacer una solicitud a una página web
    respuesta = requests.get("https://www.imdb.com")

    # Buscar el valor de la columna en la página
    if valor in respuesta.text:
        print(valor + " encontrado en la página")
    else:
        print(valor + " no encontrado en la página")
>>>>>>> 67d2e81e1f95ff01bfa8cfe6c5d935e84bd7b6e6


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




