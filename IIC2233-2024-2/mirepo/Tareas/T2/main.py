from sys import argv, exit
from entidades import (Jardin, Plantas, Solaretillo, Defensauce, Potencilantro, Aresauce,
                       Cilantrillo, Fensaulantro)

nombre_jardin = argv[1]
dificultad = argv[2]
instancia_jardin = 0

with open("data/jardines.txt", "r") as archivo:
    jardines = archivo.readlines()
    for jardin in jardines:
        jardin = jardin.strip("\n")
        jardin = jardin.split("!")
        #print(jardin[0])
        if jardin[0] == nombre_jardin:
            tablero_temporal = jardin[1].split(";")
            tablero = []
            for fila in tablero_temporal:
                fila_nueva = fila.split(",")
                tablero.append(fila_nueva)

            print(tablero)
            instancia_jardin = Jardin(tablero)
#with open("data/plantas.txt", "r") as archivo:
#    raw_plantas = 
if instancia_jardin == 0:
    print("Error, el jardín escogido no se encuentra en el archivo jardines.txt")
    exit()

while True:
    print(f"""---------------------------\n
Menú de inicio\n
---------------------------\n
Soles disponibles: {instancia_jardin.soles}\n
Temperatura: {instancia_jardin.temperatura} °C \n
Día actual: 3\n
[1] Menu Jardín\n
[2] Laboratorio\n
[3] Pasar Día\n
[0] Salir del programa\n""")
    opcion = input("ingrese el número de la opción deseada ")
    if opcion == "1":
        while True:
            print(f"""*** Este es tu Jardín Actual ***
Temperatura: {instancia_jardin.temperatura}\n""")
            for fila in instancia_jardin.tablero:
                print(fila)
            print("""\n[1] Intercambiar
[2] Cultivar
[3] Regar
[0] Volver al Menú de inicio\n""")
            j_opcion = input("Indique su opción: ")
            if j_opcion == "1":

                mensaje = "elija las dos plantas a intercambiar (formato: x1,y1;x2,y2)"
                plantas_a_mover = input(mensaje)
                if ";" not in plantas_a_mover or "," not in plantas_a_mover:
                    print("""por favor utilice el formato correcto\n""")
                else:
                    raw_posiciones = plantas_a_mover.split(";")
                    posiciones_correctas = []
                    for posicion in raw_posiciones:
                        posicion = posicion.split(",")
                        posiciones_correctas.append(posicion)
                    print(posiciones_correctas)
                    if int(posiciones_correctas[0][0]) > len(tablero) or \
int(posiciones_correctas[0][1]) > len(tablero[0]):
                        print("su seleccion no existe en el tablero")
                    else:
                        x1 = int(posiciones_correctas[0][0])
                        y1 = int(posiciones_correctas[0][1])
                        x2 = int(posiciones_correctas[1][0])
                        y2 = int(posiciones_correctas[1][1])
                        primera_planta = tablero[x1][y1]
                        segunda_planta = tablero[x2][y2]
                        tablero[x1][y1] = segunda_planta
                        print(tablero[x1][y1])
                        tablero[x2][y2] = primera_planta
                        print(tablero[x2][y2])

            if j_opcion == "2":
                planta = input("ingrese el numero de la planta que desee cultivar")
                coords = input("ingrese las coordenadas donde desee plantarla (formato x,y)")
                #instancia_jardin.cultivar_planta(planta, coords)
            if j_opcion == "0":
                break 
    
    if opcion == "2":
        print("No disponible")
    if opcion == "3":
        print("No disponible")
    if opcion == "0":
        exit()
    else:
        print("Por favor ingrese una opcion valida")
    






