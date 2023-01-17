#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt 


# In[2]:


df_movies = pd.read_csv('movies.csv') 


# In[3]:


df_ratings = pd.read_csv('ratings.csv')


# In[4]:


df_links = pd.read_csv('links.csv', dtype = object)


# In[5]:


df_tags = pd.read_csv('tags.csv')


# In[ ]:





# In[8]:


df_movies


# In[6]:


df_ratings


# In[ ]:


df_ratings


# In[10]:


df_links


# In[15]:





# In[48]:





# In[ ]:


df_tags


# In[ ]:


link = "https://www.themoviedb.org/movie/" + df_links["tmdbId"][0]


# In[ ]:


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


# In[ ]:





# In[43]:


bs = BeautifulSoup(r.content, "html.parser")


# In[44]:


print (bs.prettify)


# In[46]:


print(bs.p.get_text())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




