from functools import reduce
from itertools import product
from typing import Generator

from utilidades import Pelicula, Genero


# ----------------------------------------------------------------------------
# Parte 1: Cargar dataset
# ----------------------------------------------------------------------------

def conversion_facil(convertir_a: tuple, datos: list) -> list:
    datos_correctos = []
    for convertir, dato in zip(convertir_a, datos):
        datos_correctos.append(convertir(dato))
    return datos_correctos

def cargar_generos(ruta: str) -> Generator:
    try:
        with open(ruta, "r", encoding = "utf-8") as archivo_gen:
            for linea in archivo_gen:
                datos = linea.split(",")
                if datos[0] not in Genero._fields:
                    convertir_a = (str, int)
                    datos_correctos = conversion_facil(convertir_a, datos)
                    a_retornar = Genero(*datos_correctos)
                    yield a_retornar

    except FileNotFoundError:
        print("Error: la ruta indicada NO EXISTE :(")

def cargar_peliculas(ruta: str) -> Generator:
    try:
        with open(ruta, "r", encoding = "utf-8") as archivo_pelis:
            for linea in archivo_pelis:
                datos = linea.split(",")
                if datos[0] not in Pelicula._fields[0]:
                    convertir_a = (int, str, str, int, float)
                    datos_correctos = conversion_facil(convertir_a, datos)
                    instancia = Pelicula(*datos_correctos)
                    yield instancia

    except FileNotFoundError:
        print("Error: la ruta indicada NO EXISTE :(")


# ----------------------------------------------------------------------------
# Parte 2: Consultas sobre generadores
# ----------------------------------------------------------------------------


def obtener_directores(generador_peliculas: Generator) -> Generator:
    """
    Retorna un generador con el nombre de todos los directores.
    """
    def director(pelicula: tuple) -> str:
        return pelicula.director

    a_retornar = (map(director, generador_peliculas))
    return a_retornar


def obtener_estrenos(generador_peliculas: Generator, estreno: int) -> Generator:
    """
    Retorna un generador con el título de todas las películas cuyo
    año de entreno sea igual o mayor al entregado.
    """
    def checkeo_estreno(pelicula: tuple, estreno: int) -> str:
        if pelicula.estreno >= estreno:
            return pelicula.titulo
    pelis_sin_filtro = map(lambda y: checkeo_estreno(y, estreno), generador_peliculas)
    a_retornar = filter(lambda x: x is not None, pelis_sin_filtro)
    return a_retornar


def obtener_str_titulos(generador_peliculas: Generator) -> str:
    """
    Genera un str con todos los títulos de las películas separados por ", ".
    """
    def extractor_titulos(pelicula: tuple) -> str:
        return pelicula.titulo
    raw_titulos = filter(lambda x: x is not None, map(extractor_titulos, generador_peliculas))
    
    try:
        titulos = reduce(lambda x, y: x + ", " + y, raw_titulos)
    except TypeError:
        titulos = ""

    return titulos


def filtrar_peliculas(
    generador_peliculas: Generator,
    director: str | None = None,
    rating_min: float | None = None,
    rating_max: float | None = None,
) -> filter:
    """
    Filtra los elementos del generador de Películas según lo indicado en el input.
    """
    def filtro_director(pelicula: tuple, director: str) -> tuple:
        if pelicula.director == director:
            return pelicula

    def filtro_rating_min(pelicula: tuple, rating_min: float) -> tuple:
        if pelicula.rating >= rating_min:
            return pelicula

    def filtro_rating_max(pelicula: tuple, rating_max: float) -> tuple:
        if pelicula.rating <= rating_max:
            return pelicula

    if director is not None:
        raw_filtro = map(lambda x: filtro_director(x, director), generador_peliculas)
        filtrado = filter(lambda x: x is not None, raw_filtro)
        if rating_min is not None or rating_max is not None:
            generador_peliculas = filtrado
        else:
            return filtrado

    if rating_min is not None:
        raw_filtro = map(lambda x: filtro_rating_min(x, rating_min), generador_peliculas)
        filtrado = filter(lambda x: x is not None, raw_filtro)
        if rating_max is not None:
            generador_peliculas = filtrado
        else:
            return filtrado

    if rating_max is not None:
        raw_filtro = map(lambda x: filtro_rating_max(x, rating_max), generador_peliculas)
        filtrado = filter(lambda x: x is not None, raw_filtro)
        return filtrado




def filtrar_peliculas_por_genero(
    generador_peliculas: Generator,
    generador_generos: Generator,
    genero: str | None = None,
) -> Generator:
    """
    Crea un generador con todas las combinaciones posibles entre
    el generador de películas y el generador de géneros.
    Después, filtra las pares obtenidos y mantiene únicamente
    los que presentan el mismo id de película.
    Finalmente, retorna una lista con todos los pares pertenecientes
    a la categoría indicada.
    """
    def filtro_id(pelicula_ambos_gen: tuple) -> bool:
        if pelicula_ambos_gen[0].id_pelicula == pelicula_ambos_gen[1].id_pelicula:
            return True 
    
    def filtro_gen(pelicula_ambos_gen: tuple, genero: str) -> bool:
        if pelicula_ambos_gen[1].genero == genero:
            return pelicula_ambos_gen
        
    if genero is not None:
        gen_combinados = product(generador_peliculas, generador_generos)
        filtrado_id = filter(filtro_id, gen_combinados)
        raw_gen = map(lambda x: filtro_gen(x, genero), filtrado_id)
        filtrado_gen = filter(lambda x: x is not None, raw_gen)
        return filtrado_gen

    else:
        gen_combinados = product(generador_peliculas, generador_generos)
        filtrado_id = filter(filtro_id, gen_combinados)
        return filtrado_id


def filtrar_titulos(
    generador_peliculas: Generator, director: str, rating_min: float, rating_max: float
) -> Generator:
    """
    Genera un str con todos los títulos de las películas separados
    por ", ". Solo se consideran las peliculas que tengan el mismo
    director que el indicado, tengan un rating igual o mayor al
    rating_min y un rating igual o menor al rating_max.
    """
    a_mapear = filtrar_peliculas(generador_peliculas, director, rating_min, rating_max)
    a_retornar = obtener_str_titulos(a_mapear)
    return a_retornar
