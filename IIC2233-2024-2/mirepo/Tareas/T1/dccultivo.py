from os import path


class Predio:
    def __init__(self, codigo_predio: str, alto: int, ancho: int) -> None:
        self.codigo_predio = codigo_predio
        self.alto = alto
        self.ancho = ancho
        self.plano = []
        self.plano_riego = []
    def crear_plano(self, tipo: str) -> None:
        if tipo == "normal":
            for fila in range(self.alto):
                fila_actual = []
                for elemento_columna in range(self.ancho):
                    fila_actual.append("X")
                self.plano.append(fila_actual)
            
        elif tipo == "riego":
            for fila in range(self.alto):
                fila_actual = []
                for elemento_columna in range(self.ancho):
                    fila_actual.append(0)
                self.plano_riego.append(fila_actual)
        
        
    
    def plantar(
        self, codigo_cultivo: int, coordenadas: list, alto: int, ancho: int
    ) -> None:
        
        inicio_fil = coordenadas[0]
        inicio_col = coordenadas[1]
        disponibilidad = True
        for fila_actual in range(alto):
            for col_actual in range(ancho):
                if ((inicio_fil + fila_actual) < self.alto) and ((inicio_col + 
                                                                  col_actual) < self.ancho):
                    if self.plano[inicio_fil + fila_actual][inicio_col + col_actual] != "X":
                        disponibilidad = False
        if alto >= self.alto or ancho >= self.ancho:
            disponibilidad = False
        if disponibilidad == False:
            self.plano = self.plano


        if disponibilidad == True:
            for fila_actual in range(alto):
                for col_actual in range(ancho):
                    self.plano[inicio_fil + fila_actual][inicio_col + col_actual] = codigo_cultivo


    def regar(self, coordenadas: list, area: int) -> None:
        centro_filas = coordenadas[0]
        centro_col = coordenadas[1]
        fila_superior = centro_filas - area
        fila_inferior = centro_filas + area
        col_inicial = centro_col - area
        col_final = centro_col + area

        for alto in range(fila_superior, fila_inferior + 1):
                if ((alto == fila_superior) or (alto == fila_inferior)) and (alto >= 0 and alto <= self.alto):
                    for ancho in range(1, len(self.plano_riego[alto])):
                        self.plano_riego[alto][ancho] += 1
                        print("entra en las cotas")
                elif alto >= 0 and alto < self.alto:
                    for ancho in range(col_inicial, col_final + 1):
                        if (ancho >= 0 and ancho < len(self.plano_riego[alto])):
                            self.plano_riego[alto][ancho] += 1
                            print("entrada normal")

    def eliminar_cultivo(self, codigo_cultivo: int) -> int:
        celdas_eliminadas = 0
        for fila in range(self.alto):
            for columna in range(self.ancho):
                if self.plano[fila][columna] == codigo_cultivo:
                    self.plano[fila][columna] = "X"
                    celdas_eliminadas += 1
        return celdas_eliminadas

class DCCultivo:
    def __init__(self) -> None:
        self.predios = []

    def crear_predios(self, nombre_archivo: str) -> str:
        dir_archivo = "data/" + nombre_archivo
        if path.exists(dir_archivo) == True:
            with open(dir_archivo, "r") as archivo:
                lista_predios = archivo.readlines()
                for elemento in lista_predios:
                    datos_predio = elemento.strip("\n").split(",")
                    
                    instancia = Predio(datos_predio[0], int(datos_predio[1]), int(datos_predio[2]))
                    instancia.crear_plano("normal")
                    instancia.crear_plano("riego")
                    self.predios.append(instancia)
                    logrado = "Predios de DCCultivo cargados exitosamente"
                return logrado
        else:
            fallo = "Fallo en la carga de DCCultivo"
            return fallo
    def buscar_y_plantar(self, codigo_cultivo: int, alto: int, ancho: int) -> bool:
        pass
        logrado = False
        totalidad_espacio_disponible = 0
        inicio_col = 0
        inicio_fil = 0
        for predio in self.predios:
            en_predio_actual = True
            predio.plantar(codigo_cultivo, [inicio_fil, inicio_col], alto, ancho)
            area_total = alto * ancho
            for fila_actual in range(alto):
                for col_actual in range(ancho):
                    if predio.plano[fila_actual][col_actual] == codigo_cultivo:
                        totalidad_espacio_disponible += 1
            if totalidad_espacio_disponible == (alto*ancho):
                logrado = True
                return logrado


            
            while logrado == False and en_predio_actual == True:
                print("entra en while")
                totalidad_espacio_disponible = 0 
                inicio_col += 1
                if inicio_fil >= len(predio.plano) - 1:
                    print("condicion fracaso")
                    en_predio_actual = False
                if inicio_col == (len(predio.plano[inicio_fil])):
                    print("condicion avanzar fila")
                    inicio_fil += 1
                if ((predio.alto - inicio_fil) >= alto) and ((predio.ancho - inicio_col) >= ancho):
                    print("")
                    for fila_actual in range(alto):
                        for col_actual in range(ancho):
                            if predio.plano[inicio_fil + fila_actual][inicio_col
                                                                      + col_actual] != "X":
                                logrado = False
                            elif predio.plano[inicio_fil + fila_actual][inicio_col
                                                                        + col_actual] == "X":
                                totalidad_espacio_disponible += 1
                    if totalidad_espacio_disponible == (alto * ancho):
                        for fila_actual in range(alto):
                            for col_actual in range(ancho):
                                predio.plano[inicio_fil + fila_actual][inicio_col
                                                                    + col_actual] = codigo_cultivo
                        logrado = True
                        return logrado

    def buscar_y_regar(self, codigo_predio: str, coordenadas: list, area: int) -> None:
        pass

    def detectar_plagas(self, lista_plagas: list[list]) -> list[list]:
        pass
