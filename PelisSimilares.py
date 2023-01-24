#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.read_csv("ratings.csv", encoding='latin-1', usecols=['userId', 'movieId', 'rating'])
#users = pd.read_csv("Usuario_0.csv", encoding='latin-1' ,usecols=['movieId', 'title', 'rating'])
movies = pd.read_csv("movies.csv", encoding='latin-1' ,usecols=['movieId', 'title', 'genres'])

def weighted_average_score(df, k=0.8):
    n_views = df.groupby('movieId', sort=False).movieId.count()
    ratings = df.groupby('movieId', sort=False).rating.mean()
    scores = ((1-k)*(n_views/n_views.max()) + 
              k*(ratings/ratings.max())).to_numpy().argsort()[::-1]
    df_deduped = df.groupby('movieId', sort=False).agg({'title':'first', 
                                                         'genres':'first', 
                                                         'rating':'mean'})
    return df_deduped.assign(views=n_views).iloc[scores]

df = movies.merge(ratings)
weighted_average_score(df).head(10)

genre_popularity = (movies.genres.str.split('|')
                      .explode()
                      .value_counts()
                      .sort_values(ascending=False))

tf = TfidfVectorizer(analyzer=lambda s: (c for i in range(1,4)
                                             for c in combinations(s.split('|'), r=i)))
tfidf_matrix = tf.fit_transform(movies['genres'])

cosine_sim = cosine_similarity(tfidf_matrix)

cosine_sim_df = pd.DataFrame(cosine_sim, index=movies['title'], columns=movies['title'])

def genre_recommendations(i, M, items, k=10):
    """
    Recommends movies based on a similarity dataframe

    Parameters
    ----------
    i : str
        Movie (index of the similarity dataframe)
    M : pd.DataFrame
        Similarity dataframe, symmetric, with movies as indices and columns
    items : pd.DataFrame
        Contains both the title and some other features used to define similarity
    k : int
        Amount of recommendations to return

    """
    ix = M.loc[:,i].to_numpy().argpartition(range(-1,-k,-1))
    closest = M.columns[ix[-1:-(k+2):-1]]
    closest = closest.drop(i, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)

genre_recommendations('Coco (2017)', cosine_sim_df, movies[['title', 'genres']])
