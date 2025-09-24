from typing import Any, Generator, Iterable
from utilidades import Pizzas, Locales, ContenidoPedidos, Pedidos
from os import path
from itertools import product, groupby, count
from functools import reduce
from collections import defaultdict

# Carga de datos
def conversion(convertir_a: tuple, datos: list) -> list:
    datos_correctos = []
    for convertir, dato in zip(convertir_a, datos):
        datos_correctos.append(convertir(dato))
    return datos_correctos

def cargar_pizzas(path: str) -> Generator:
    with open(path, "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            raw_data = linea.strip("\n").split(",")
            if raw_data[0].lower() not in Pizzas._fields:
                tipo_datos = (str, str, int)
                datos_corregidos = conversion(tipo_datos, raw_data)
                tupla_pizza = Pizzas(*datos_corregidos)
                yield tupla_pizza

def cargar_locales(path: str) -> Generator:
    with open(path, "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            raw_data = linea.strip("\n").split(",")
            if raw_data[0].lower() not in Locales._fields:
                tipo_datos = (int, str, str, str, int)
                datos_corregidos = conversion(tipo_datos, raw_data)
                tupla_local = Locales(*datos_corregidos)
                yield tupla_local

def cargar_pedidos(path: str) -> Generator:
    with open(path, "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            raw_data = linea.strip("\n").split(",")
            if raw_data[0].lower() not in Pedidos._fields:
                tipo_datos = (int, int, int, str, str)
                datos_corregidos = conversion(tipo_datos, raw_data)
                tupla_pedidos = Pedidos(*datos_corregidos)
                yield tupla_pedidos

def cargar_contenido_pedidos(path: str) -> Generator:
    with open(path, "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            raw_data = linea.strip("\n").split(",")
            if raw_data[0].lower() not in ContenidoPedidos._fields:
                tipo_datos = (int, str, int, float)
                datos_corregidos = conversion(tipo_datos, raw_data)
                tupla_content = ContenidoPedidos(*datos_corregidos)
                yield tupla_content


# Consultas que ocupan 1 generador

def pedidos_con_al_menos_esta_pizza(
        generador_contenido_pedidos: Generator,
        tipo_de_pizza: str
        ) -> Iterable:
    iterable_pedidos = []
    for pedido in generador_contenido_pedidos:
        solo_nombre = pedido.nombre.split("_")
        if tipo_de_pizza == solo_nombre[0]:
            iterable_pedidos.append(pedido)
    return iterable_pedidos

def cantidad_vendida_de_pizza_por_tipo(
        generador_contenido_pedidos: Generator,
        tipo_de_pizza: str
        ) -> int:
    cantidad = int(0)
    for pedido in generador_contenido_pedidos:
        solo_nombre = pedido.nombre.split("_")
        if tipo_de_pizza == solo_nombre[0]:
            cantidad += pedido.cantidad        
    return cantidad

def pedido_con_mayor_descuento_utilizado(
        generador_contenido_pedidos: Generator
        ) -> Iterable:
    pedidos_mayor_dcto = []

    for pedido in generador_contenido_pedidos:
        if len(pedidos_mayor_dcto) == 0:
            pedidos_mayor_dcto.append(pedido)
        elif pedido.descuento > pedidos_mayor_dcto[0].descuento:
            pedidos_mayor_dcto = []
            pedidos_mayor_dcto.append(pedido)
        elif pedido.descuento == pedidos_mayor_dcto[0].descuento:
            pedidos_mayor_dcto.append(pedido)
    return pedidos_mayor_dcto

def ajustar_precio_segun_ingredientes(
        generador_pizzas: Generator,
        ingrediente: str,
        diferencia_precio: int
        ) -> Iterable:
    iterable_pizzas = []
    for pizza in generador_pizzas:
        check_ingredientes = pizza.ingredientes.split(";")
        if ingrediente in check_ingredientes:
            nuevo_precio = pizza.precio + diferencia_precio
            if nuevo_precio < 7000:
                nuevo_precio = 7000
            nueva_inst = Pizzas(pizza.nombre, pizza.ingredientes, nuevo_precio)
            iterable_pizzas.append(nueva_inst)
    return iterable_pizzas

def clientes_despues_hora(
        generador_pedidos: Generator,
        hora: str
        ) -> str:
    lista_pedidos = []
    desde_hora = hora.split(":")
    for pedido in generador_pedidos:
        hora_pedido = pedido.hora.split(":")
        if hora_pedido[0] > desde_hora[0]:
            lista_pedidos.append(str(pedido.id_cliente))
        elif hora_pedido[0] == desde_hora[0]:
            if hora_pedido[1] >= desde_hora[1]:
                lista_pedidos.append(str(pedido.id_cliente))
    a_retornar = " ".join(lista_pedidos)
    return a_retornar

def cliente_indeciso(
        generador_pizzas: Generator,
        ingrediente_no_deseado: str,
        cantidad_pizzas: int
        ) -> Iterable:
    pizzas_cliente = []
    for pizza in generador_pizzas:
        if len(pizzas_cliente) == cantidad_pizzas:
            return pizzas_cliente
        elif ingrediente_no_deseado not in pizza.ingredientes:
            pizzas_cliente.append(pizza)
    if len(pizzas_cliente) == 0:
        return pizzas_cliente
    elif len(pizzas_cliente) < cantidad_pizzas:
        current_diff = cantidad_pizzas - len(pizzas_cliente)
        for _ in range(current_diff):
            pizza_a_agregar = pizzas_cliente[_]
            pizzas_cliente.append(pizza_a_agregar)
        return pizzas_cliente
            
def pizzas_con_ingrediente(
        generador_pizzas: Generator,
        ingrediente: str
        ) -> Iterable:
    con_ingrediente = []
    for pizza in generador_pizzas:
        ingredientes = pizza.ingredientes.split(";")
        if ingrediente in ingredientes:
            con_ingrediente.append(pizza)
    return con_ingrediente

def pizzas_pagables_de_un_tamano(
        generador_pizzas: Generator,
        dinero: int,
        tamano: str
    ) -> Iterable:
    pizzas_pagables = []
    for pizza in generador_pizzas:
        info_pizza = pizza.nombre.split("_")
        if pizza.precio <= dinero and info_pizza[1] == tamano:
            pizzas_pagables.append(pizza)
    return pizzas_pagables

def cantidad_empleados_pais(
        generador_locales: Generator,
        pais: str
        ) -> int:
    cantidad_empleados = 0
    for local in generador_locales:
        if local.pais == pais:
            cantidad_empleados += local.cantidad_trabajadores
    return cantidad_empleados


# Consultas que ocupan 2 Generadores
def calculo_ganancias(ambos_gen: tuple) -> list:
    pedido = ambos_gen[0]
    pizza = ambos_gen[1]
    
    id_pedido = pedido.id_pedido
    if pedido.nombre == pizza.nombre:
        precio_pre = pedido.cantidad * pizza.precio * (1 - pedido.descuento)
        precio_final = round(precio_pre)
        a_retornar = (id_pedido, precio_final)
        return a_retornar

def ganancias_producidas_en_los_pedidos(
        generador_contenido_pedidos: Generator,
        generador_pizzas: Generator
        ) -> Iterable:
    
    
    def suma_ganancias(tupla: tuple) -> tuple:
        id_pedido = tupla[0]
        #iter_ganancias = tupla[1]
        suma_ganancias = sum(map(lambda x: x[1], tupla[1]))
        #suma_ganancias = sum(map(lambda x: x[1], tupla[1]))
        #suma_ganancias = sum(ganancias_per_tupla)
        #if id_pedido == 5:
        print(id_pedido, suma_ganancias)
        #a_retornar = (tupla[0], suma_ganancias)
        return tupla[0], suma_ganancias
    
    return gen

def pizza_mas_vendida_del_dia(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        fecha: str
        ) -> set:

    def checkeo_pedido(tupla_por_id: tuple) -> defaultdict:
        dic_pizzas = defaultdict(int)
        for contenido in tupla_por_id:
            for instancia in contenido[1]:
                nom_pizza = instancia.nombre.split("_")[0]
                #print(nom_pizza)
                cantidad = int(instancia.cantidad)
                dic_pizzas[nom_pizza] += cantidad
        #print(dic_pizzas)
        return dic_pizzas

    
    pedidos_filtrados = filter(lambda x: x.fecha == fecha, generador_pedidos)

    gen_content_agrupado = groupby(generador_contenido_pedidos, key=lambda x: x.id_pedido)
    def filtro_id(pedidos: Generator, gen_agrupado: Iterable) -> Generator:
        for pedido in pedidos:
            for grupo in gen_agrupado:
                if pedido.id_pedido == grupo[0]:
                    #print(grupo)
                    yield grupo
    gen_contenido_correcto = filtro_id(pedidos_filtrados, gen_content_agrupado)
              
    
    dic_a_checkear = checkeo_pedido(gen_contenido_correcto)
    
    inicio_pizza = []
    cantidad_ini = 0
    for pizza in dic_a_checkear:
        #print(pizza)
        #print(dic_a_checkear[pizza])
        cantidad = dic_a_checkear[pizza]
        if cantidad > cantidad_ini: 
            str_pizza = str(pizza)
            inicio_pizza = [str_pizza]
            cantidad_ini = cantidad
            #print(str_pizza)
            #print(inicio_pizza)
        elif cantidad == cantidad_ini:
            inicio_pizza.append(str(pizza))
            #print(inicio_pizza)
    
    #print(type(inicio_pizza))
    #print(inicio_pizza)
    return set(inicio_pizza)
    

def pizza_del_mes(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        mes: str
        ) -> str:
    pass

def popularidad_mezcla_de_ingredientes(
        generador_pizzas: Generator,
        generador_contenido_pedidos: Generator,
        ingredientes: set
        ) -> int:
    pass


def total_ahorrado_pedidos(
        generador_contenido_pedidos: Generator,
        generador_pizzas: Generator
        ) -> str:
    pass

def pizza_favorita_cliente(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        id_cliente: int,
        ) -> tuple:
    pass


# Consultas que ocupan 3 o mas Generadores

def local_mas_pizzas_vendidas_por_tipo_de_pizza(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        tipo_de_pizza: str
        ) -> Iterable:
    pass

def ganancia_total_de_un_local(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_pizzas: Generator,
        id_local: int
        ) -> int:
    pass


def promedio_ventas_con_descuento_de_un_pais(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        pais: str
        ) -> float:
    pass


def gasto_cliente_por_mes(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_pizzas: Generator,
        id_cliente: int,
        year: int,
        ) -> list:
    pass

def pizzas_vendidas_mes_pais(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        pais: str,
        mes: int,
        year: int,
        ) -> int:
    pass


# Consulta anidada

def consulta_anidada(instrucciones: dict) -> Any:
    pass
