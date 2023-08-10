from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
app = FastAPI()

'''
origins = ["*"]
app.add_middleware(
     CORSMiddleware,
     allow_origins = True,
     allow_credentials = True,
     allow_methods = ["*"],
     allow_headers = ["*"]
)
'''

df = pd.read_csv('movies_dataset_ETL.csv',delimiter=',', header=0)

'''
Se ingresa un idioma (como están escritos en el dataset,
no hay que traducirlos!). Debe devolver la cantidad de
películas producidas en ese idioma.
'''
@app.get('/idioma')
async def peliculas_idioma(idioma: str ):
    count = df[df['original_language'] == idioma].shape[0]
    return {"message": f"Cantidad de películas en el idioma {idioma} : {count}"}

'''
Se ingresa una pelicula. Debe devolver la duracion y el año.
'''

@app.get('/duracion')
async def peliculas_duracion( Pelicula: str):
     pelicula = df[df['title'] == Pelicula]
     if pelicula.empty:
          return {"message" : f"No se encontro la película {Pelicula}"}
     duracion = pelicula['runtime'].values[0]
     ano = pelicula['release_year'].values[0]
     return {f"La pelicula {Pelicula}, tiene una duración de {duracion} Min y fue estrenada el año {ano}"}
'''
Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
'''

@app.get('/franquicia')
async def franquicia(Franquicia: str ):
     peliculas_franquicia = df[df['name_btc'] == Franquicia]
     cantidad_peliculas = peliculas_franquicia.shape[0]
     if cantidad_peliculas == 0:
          return {"message" : f"No se encontraron franquicias por el nombre {Franquicia}"}
     ganancia_total = (peliculas_franquicia['revenue'] - peliculas_franquicia['budget']).sum()
     return {"message" : f"La franquicia {Franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio {ganancia_total/cantidad_peliculas}"}

'''
Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), 
retornando la cantidad de peliculas producidas en el mismo.
'''

@app.get('/pais')
async def peliculas_pais( Pais: str ):
     pais= df[df['country_name'] == Pais].shape[0]     
     return {"message": f"Cantidad de películas en el idioma '{Pais}': {pais}"}

'''
Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo. 
'''

@app.get('/productora')
async def productoras_exitosas( Productora: str):
     peliculas = df[df['ption_companies_name'] == Productora]
     cantidad_peliculas = peliculas.shape[0]
     revenue = peliculas['revenue'].sum()
     return {"message" : f"Cantidad de peliculas producidas por la productora '{Productora}' fue {cantidad_peliculas} y el revenue {revenue} "}

'''
 Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver 
 el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada 
 película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.
'''

@app.get('/director')
def get_director( nombre_director):
    return {"message" : "información global de peliculas"} 

'''
Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.
'''

@app.get('/recomendacion')
def recomendacion( titulo ):
     return {"message" : "Peliculas similares"}
     
     


