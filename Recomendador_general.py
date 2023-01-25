import pandas as pd
from itertools import combinations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Lectura de los CSV
ratings = pd.read_csv("ratings.csv", encoding='latin-1', usecols=['userId', 'movieId', 'rating'])
movies = pd.read_csv("movies.csv", encoding='latin-1' ,usecols=['movieId', 'title', 'genres'])

#Creacion del vector TF-IDF
tf = TfidfVectorizer(analyzer=lambda s: (c for i in range(1,4)
                                             for c in combinations(s.split('|'), r=i)))
tfidf_matrix = tf.fit_transform(movies['genres'])

cosine_sim = cosine_similarity(tfidf_matrix)

cosine_sim_df = pd.DataFrame(cosine_sim, index=movies['title'], columns=movies['title'])

#Funcion que devuelve el ranking de las peliculas similares 
def genre_recommendations(i, M, items, k=10):
    ix = M.loc[:,i].to_numpy().argpartition(range(-1,-k,-1))
    closest = M.columns[ix[-1:-(k+2):-1]]
    closest = closest.drop(i, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)