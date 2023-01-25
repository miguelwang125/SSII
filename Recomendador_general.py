#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[53]:


ratings = pd.read_csv("ratings.csv", encoding='latin-1', usecols=['userId', 'movieId', 'rating'])
movies = pd.read_csv("movies.csv", encoding='latin-1' ,usecols=['movieId', 'title', 'genres'])


# In[54]:


tf = TfidfVectorizer(analyzer=lambda s: (c for i in range(1,4)
                                             for c in combinations(s.split('|'), r=i)))
tfidf_matrix = tf.fit_transform(movies['genres'])


# In[67]:


cosine_sim = cosine_similarity(tfidf_matrix)


# In[68]:


cosine_sim_df = pd.DataFrame(cosine_sim, index=movies['title'], columns=movies['title'])


# In[69]:


ratings = pd.read_csv("ratings.csv", encoding='latin-1', usecols=['userId', 'movieId', 'rating'])
movies = pd.read_csv("movies.csv", encoding='latin-1' ,usecols=['movieId', 'title', 'genres'])


# In[73]:


def genre_recommendations(i, M, items, k=10):
    ix = M.loc[:,i].to_numpy().argpartition(range(-1,-k,-1))
    closest = M.columns[ix[-1:-(k+2):-1]]
    closest = closest.drop(i, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)


# In[74]:


movies[movies.title.eq('Toy Story (1995)')]


# In[75]:


genre_recommendations('Coco (2017)', cosine_sim_df, movies[['title', 'genres']])


# In[ ]:





# In[ ]:




