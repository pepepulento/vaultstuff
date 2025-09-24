# Tarea 3: Little DCCaesars 🧟🍕

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. No utilicé codigo de fuentes externas, sin embargo, fueron usadas explicaciones de https://docs.python.org/3/library/itertools.html en la realización del archivo consultas.py

# Actualizaciones Tarea

> 1 de octubre
1. Se hace un cambio en el enunciado, se agrega el formulario de entregas atrasadas.
2. Se hace un cambio en el enunciado, se explica que la forma de evaluar los tests es ternaria.

> 2 de octubre
1. Se hace un cambio en los tests públicos de la función pizzas_con_ingrediente. Cuando la función recibía el ingrediente "champiñones", 
la solución contenía pizzas que tenían "salsa de champiñones" siendo que eran dos ingredientes distintos. Ahora el test esta arreglado.
2. Se hace un cambio menor en el enunciado, en la función clientes_despues_hora se recibe la hora en formato "HH:MM" y no en formato "HH"

> 5 de octubre
1. Se agregó "timeout" en todos los tests: test_12_pizza_del_mes_carga_datos
2. Ajuste tests funciones ajustar_precio_segun_ingredientes y popularidad_mezcla_de_ingredientes. Se agregaron tests que verifican funcionamiento 
correcto cuando se tienen ingredientes que son substrings de otros ingredientes. Por ejemplo, al tener "tomate" como ingrediente, no considerar pizzas 
que tienen "salsa de tomate" y no "tomate". Este ajuste está relacionado con el ajuste número 1 del día 2 de octubre.

> 11 de octubre
1. Se arreglaron los datos de los tests de correctitud que recibían generadores de pedidos. Antes la información de la hora del pedido se encontraban 
en formato HH:MM, ahora se encuentran en formato HH:MM:SS tal como se encuentran estos datos en los archivos csv. Se arregló la desconcordancia entre 
tests de correctitud y tests de carga de datos (los tests de carga de datos sí respetaban el formato HH:MM:SS)