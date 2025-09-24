import collections
from os.path import join
from utilidades import Anime  # Debes utilizar esta nametupled


#####################################
#       Parte 1 - Cargar datos      #
#####################################
def cargar_animes(ruta_archivo: str) -> list:
    with open(ruta_archivo, "r", encoding = "utf-8") as archivo:
        raw_data_animes = archivo.read()
        lista_animes = raw_data_animes.split("\n")
        
    lista_tuplas = []
    for anime in lista_animes:
        anime_unico = anime.split(",")
        
        if len(anime_unico) == 6:
            convertir_a_set = anime_unico[5].split(";")
            
            anime_unico[5] = set(convertir_a_set)
            anime_unico[1] = int(anime_unico[1])
            anime_unico[2] = int(anime_unico[2])
            anime_unico[3] = int(anime_unico[3])
        
            tupla_anime = Anime(anime_unico[0], anime_unico[1],
                                anime_unico[2], anime_unico[3], anime_unico[4], anime_unico[5])
            
            lista_tuplas.append(tupla_anime)
            
    return lista_tuplas


#####################################
#        Parte 2 - Consultas        #
#####################################
def animes_por_estreno(animes: list) -> dict:
    dict_animes = {}
    for anime in animes:
        llave = anime.estreno
        if llave not in dict_animes:
            dict_animes[int(llave)] = [anime.nombre]
        elif llave in dict_animes:
                dict_animes[int(llave)].append(anime.nombre)
    
    return dict_animes


def descartar_animes(generos_descartados: set, animes: list) -> list:
    lista_aceptados = []
    for anime in animes:
        descartar = False
        for genero in anime.generos:
            if genero in generos_descartados:
                descartar = True
        if descartar == False:
            lista_aceptados.append(anime.nombre)

    return lista_aceptados


def resumen_animes_por_ver(*animes: Anime) -> dict:
    
    dict_resumen = {"puntaje promedio": float(0), "capitulos total": 0, "generos": set()}
    
    for anime in animes:
        dict_resumen["puntaje promedio"] += float(anime.puntaje)
        dict_resumen["capitulos total"] += int(anime.capitulos)
        for genero in anime.generos:
            dict_resumen["generos"].add(genero)
    if len(animes) != 0:
        dict_resumen["puntaje promedio"] = dict_resumen["puntaje promedio"]/len(animes)
        dict_resumen["puntaje promedio"] = round(dict_resumen["puntaje promedio"], 1)
    return dict_resumen


def estudios_con_genero(genero: str, **estudios: list) -> list:
    
    estudios_con_genero = []
    if len(estudios) != 0:
        
        for estudio in estudios:
            
            for anime in estudios[estudio]:
                
                if genero in anime.generos:
                    
                    if anime.estudio not in estudios_con_genero:
                        estudios_con_genero.append(estudio)
                        

    return estudios_con_genero


if __name__ == "__main__":
    #####################################
    #       Parte 1 - Cargar datos      #
    #####################################
    animes = cargar_animes(join("data", "ejemplo.chan"))
    indice = 0
    for anime in animes:
        print(f"{indice} - {anime}")
        indice += 1

    #####################################
    #        Parte 2 - Consultas        #
    #####################################
    # Solo se usará los 2 animes del enunciado.
    datos = [
        Anime(
            nombre="Hunter x Hunter",
            capitulos=62,
            puntaje=9,
            estreno=1999,
            estudio="Nippon Animation",
            generos={"Aventura", "Comedia", "Shonen", "Acción"},
        ),
        Anime(
            nombre="Sakura Card Captor",
            capitulos=70,
            puntaje=10,
            estreno=1998,
            estudio="Madhouse",
            generos={"Shoujo", "Comedia", "Romance", "Acción"},
        ),
    ]

    # animes_por_estreno
    estrenos = animes_por_estreno(datos)
    print(estrenos)

    # descartar_animes
    animes = descartar_animes({"Comedia", "Horror"}, datos)
    print(animes)

    # resumen_animes_por_ver
    resumen = resumen_animes_por_ver(datos[0], datos[1])
    print(resumen)

    # estudios_con_genero
    estudios = estudios_con_genero(
        "Shonen",
        Nippon_Animation=[datos[0]],
        Madhouse=[datos[1]],
    )
    print(estudios)
