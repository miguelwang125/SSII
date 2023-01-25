import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def predecir_puntuacion(film):
    # Lectura de los de CSV
    usuario = pd.read_csv("Usuario_0.csv")
    movies = pd.read_csv("movies.csv")
   
    #juntar los dos dataframe = pelis vistas por el usuario 
    peliculas_vistas = pd.merge(usuario, movies, on='movieId') 

    # se crea una matriz con los generos que hay 
    coun_vect = CountVectorizer()
    count_matrix = coun_vect.fit_transform(peliculas_vistas["genres"])
    
    #X = generos de pelis vistas
    X= count_matrix

    # Entrenamiento del modelo con regresion lineal
    
    # y = rating de las pelis vistas
    y = peliculas_vistas["rating"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression().fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    prueba = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

    # Seleccionar la película con el título
    peliculas_novistas = movies[movies["title"]== film]

    # Vectorizar la pelicula elegida
    peliculas_novistas_vectorized = coun_vect.transform(peliculas_novistas["genres"])
    
    count_array_ = peliculas_novistas_vectorized.toarray()
    noVista = pd.DataFrame(data=count_array_,columns = coun_vect.get_feature_names_out())
    
    # predecir la puntuación de la pelicula seleccionada
    predicted_rating = model.predict(noVista)
    return predicted_rating

def RecomendacionDadoUsuario():
    
    # Lectura de los de CSV
    usuario = pd.read_csv("Usuario_0.csv")
    movies = pd.read_csv("movies.csv")

    # juntar los dos dataframe = pelis vistas por el usuario
    peliculas_vistas = pd.merge(usuario, movies, on='movieId')

    # Crear una instancia del vectorizador
    coun_vect = CountVectorizer()

    # se crea una matriz con los generos que hay
    count_matrix = coun_vect.fit_transform(peliculas_vistas["genres"])

    # Entrenamiento del modelo con regresion lineal (otra opción RandomForestRegressor)
    X = count_matrix
    y = peliculas_vistas["rating"]

    # Se crea el modelo y se entrena 
    model = RandomForestRegressor().fit(X, y)

    # Crea una nueva lista, donde se almacena las películas puntuadas por el usuario_0
    ratings_usuario = usuario["movieId"].tolist()

    # Filtra las películas no ha puntuadas el usuario_0
    movies_noRatings = movies[~movies["movieId"].isin(ratings_usuario)]


    # Vectorizar las peliculas no vistas para poder predecir su puntuacion
    X_no_vistas = coun_vect.transform(movies_noRatings["genres"])
    

    # predecir la puntuacion de las peliculas no vistas
    y_pred = model.predict(X_no_vistas)

    # añade la puntuacion predicha al dataframe de peliculas no vistas
    movies_noRatings["predicted_rating"] = y_pred

    # ordena el dataframe por la puntuacion predicha para obtener un ranking, los mas altos son los mas recomendados
    movies_noRatings = movies_noRatings.sort_values(by="predicted_rating", ascending=False)

    # imprime las 10 primeras peliculas luego de ser ordenadas, estas son las recomendadas
    return movies_noRatings["title"].head(10)