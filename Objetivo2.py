#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


# In[4]:


def predecir_puntuacion():
    # Lectura de los de CSV
    usuario = pd.read_csv("Usuario_0.csv")
    movies = pd.read_csv("movies.csv")
   
    #juntar los dos dataframe = pelis vistas por el usuario 
    peliculas_vistas = pd.merge(usuario, movies, on='movieId') 

    # Crear una instancia del vectorizador
    vectorizer = CountVectorizer()

    # se crea una matriz con los generos que hay 
    coun_vect = CountVectorizer()
    count_matrix = coun_vect.fit_transform(peliculas_vistas["genres"])
    count_array = count_matrix.toarray()
    #print(count_array)
    dfVec = pd.DataFrame(data=count_array,columns = coun_vect.get_feature_names_out())
    X= dfVec
    #print(X)
    print(X.shape)
    

    # Entrenamiento del modelo con regresion lineal (otra opción RandomForestRegressor) 
    y = peliculas_vistas["rating"]
    #print(y)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model =LinearRegression().fit(X_train, y_train)
    
    y_pred = model.predict(X_test)

    prueba = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(prueba)
    
    # score = precisión del modelo
    print("score: ")
    print(model.score(X_test, y_test))

    # Seleccionar la película con el título
    peliculas_novistas = movies[movies["title"]== "Grumpier Old Men (1995)"]

    # Vectorizar la pelicula elegida
    peliculas_novistas_vectorized = coun_vect.transform(peliculas_novistas[["genres"]])
    count_array_ = peliculas_novistas_vectorized.toarray()
    noVista = pd.DataFrame(data=count_array_,columns = coun_vect.get_feature_names_out())

    # predecir la puntuación de la pelicula seleccionada
    predicted_rating = model.predict(noVista)
    print(predicted_rating)
          
predecir_puntuacion()



def RecomendacionDadoUsuario():
        # Carga del CSV 
        df_movies = pd.read_csv("movies.csv")

        # Carga del CSV 
        df_usuario_0 = pd.read_csv("Usuario_0.csv")

        # Crea una nueva lista, donde se almacena las películas puntuadas por el usuario_0
        ratings_usuario = df_usuario_0["movieId"].tolist()

        # Filtra las películas no ha puntuadas el usuario_0
        movies_noRatings = df_movies[~df_movies["movieId"].isin(ratings_usuario)]

        # Recomienda las primeras 10 películas no puntuadas
        recomedacion = movies_noRatings.head(10)

        for i, j in recomedacion.iterrows():
            genre = j["genres"].split("|")[0]
            print(recomedacion)
            
RecomendacionDadoUsuario()


# In[ ]:





# In[ ]:





# In[ ]:




