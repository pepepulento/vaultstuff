from sys import exit
from utils import imprimir_planos, plagas
from dccultivo import Predio, DCCultivo
while True:
    print("""¡Bienvenido a DCCultivo!\n
          \n*** Menú de Inicio ***\n
          \n[1] Crear Predios\n[2] Salir del programa\n
          \n""")
    opcion = input("Indique su opción (1, 2): ")
    if opcion == "1":
        archivo = input("escriba el nombre del archivo a abrir (incluyendo su extensión) ")
        instancia = DCCultivo()
        string_logrado = instancia.crear_predios(archivo)
        if string_logrado == "Fallo en la carga de DCCultivo":
            print("""\nerror, archivo no encontrado\n""")
            
        else:
            while True:
                print("""¡Bienvenido a DCCultivo!\n
Tu terreno está listo para trabajar.\n\n
*** Menú de Acciones ***\n\n
[1] Visualizar predio\n
[2] Plantar\n
[3] Regar\n
[4] Buscar y eliminar plagas\n
[5] Salir del programa\n""")
                opcion = input("Indique su opción (1, 2, 3, 4, 5): ")
                if opcion == "1":
                    predio = input("Ingrese el código del predio a visualizar ")
                    encontrado = False
                    for predios in instancia.predios:
                        if predio == predios.codigo_predio:
                            imprimir_planos(predios)
                            encontrado = True
                    if encontrado == False:
                        print("""\nno se ha encontrado un predio con ese código :(\n""")
                if opcion == "2":
                    codigo_cultivo = int(input("Ingrese el código del cultivo a plantar: "))
                    alto = int(input("Ingrese el alto a cultivar "))
                    ancho = int(input("Ingrese el ancho a cultivar "))
                    logro = instancia.buscar_y_plantar(codigo_cultivo, alto, ancho)
                    if logro:
                        print("Cultivo plantado con exito\n")
                    elif logro == False:
                        print("No se pudo plantar el cultivo\n")
                if opcion == "3":
                    codigo_predio = input("Ingrese el código del predio a regar ")
                    coordenadas = input("Ingrese las coordenadas (en formato 1,2 por favor) ")
                    area = int(input("Ingrese el area a regar "))
                    lista_coords = coordenadas.split(",")
                    for elemento in range(len(lista_coords)):
                        lista_coords[elemento] = int(lista_coords[elemento])
                    instancia.buscar_y_regar(codigo_predio, lista_coords, area)
                if opcion == "4":
                    retornado = plagas(instancia)
                    resultado = instancia.detectar_plagas(retornado)
                    print(resultado)
                    print("\nbusqueda y deteccion de plagas activado satisfactoriamente\n")
                if opcion == "5":
                    print("El programa se cerrará, ¡adios!")
                    exit()


    elif opcion == "2":
        print("El programa se cerrará, ¡adios!")
        exit()
    else:
        print("""\nPor favor, ingrese una opción correcta\n""")

