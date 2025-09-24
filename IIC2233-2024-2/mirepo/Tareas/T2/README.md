# Tarea 2: DCCampesino 🌻🧟

#### Programación Orientada a Objetos: 16 pts (10%)
##### 🟠 Definición de clases, herencia y *properties*
Todas las clases están declaradas con sus metodos abstractos y regulares, además, las clases heredan de una clase base (la cual *no* es instanciable por si misma) Planta, y las plantas que resultan de combinar dos tambien heredan de esas respectivas clases, en la clase Defensauce se hace overriding del metodo .setter del atributo vida, dado su atributo armadura

#### Preparación del programa: 6 pts (4%)
##### ✅ Inicio de la partida
el programa recibe correctamente los argumentos por consola, y los utiliza

#### Entidades: 64 pts (39%)
##### 🟠 Jardín
Jardín posee todos sus atributos, sin embargo, los metodos mutar y presentarse no se encuentran desarrollados
##### 🟠 Plantas
La clase plantas y las clases que heredan de ella poseen todos sus metodos y atributos correspondientes implementados, sin embargo, dado que no se completó la simulación de dia la implementación de la caracteristica del Potencilantro (y en consecuencia del Cilantrillo)puede no ser la adecuada

#### Flujo del programa: 40 pts (24%)
##### ✅ Menú de Inicio
Existe un menú de inicio robusto, que permite salir del programa y avisa al usuario en caso de ingresar una opción no valida
##### 🟠 Menú Jardín
Existe un menú jardin, en el cual se puede ver la temperatura actual del jardin, junto con una representación del jardín como tablero, además se pueden intercambiar plantas dentro del jardín, sin embargo, no se puede cultivar, tampoco regar las plantas, ni utilizar los metodos no completados (mutar y presentarse)
##### ❌ Laboratorio
No fue implementado
##### ❌ Fin del juego
Pasar dia no fue implementado
##### ✅ Robustez
Los inputs se manejan correctamente, y se indica en caso de algun problema de formato o si no se entrega una opción valida, el programa no se cae por este motivo

#### Simular día: 23 pts (14%)
##### ❌ Temperatura
No fue implementado
##### ❌ Eventos
No fue implementado
##### ❌ Calcular soles
No fue implementado
##### ❌ Llegada de plantas
No fue implementado
##### ❌ Presentación
No fue implementado

#### Archivos: 15 pts (9%)
##### 🟠 Archivos.txt
Se abre correctamente el archivo jardines.txt en la carpeta data, y sus datos se utilizan para la selección del tablero, sin embargo, no se crea un inventario a partir de plantas.txt ni se utiliza eventos.txt
##### ✅ parametros.py
Se crea el archivo parametros.py en su totalidad, con los parametros solicitados

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```data/``` en ```raíz```
2. ```jardines.txt``` en ```data/```
3. ```entidades.py``` en ```raíz```
4. ```parametros.py``` en ```raíz```
 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```argv, exit```
2. ```abc```: ```ABC, abstractmethod```
3. ```random```: ```randint```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```entidades.py```: Contiene a ```Jardin```, ```Plantas```, ```Solaretillo```, ```Defensauce```, ```Potencilantro```, ```Aresauce```, ```Cilantrillo```, ```Fensaulantro```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Existe una carpeta llamada data/ en el mismo nivel que el archivo main.py, es valido pues en el enunciado no se especifica que los archivos se encuentren en otra direccion/a>
2. <Dentro de la carpeta data/ existirán archivos llamados jardines.txt, plantas.txt y eventos.txt, es valido porque en el enunciado se especifica que se requiere robustez en la recolección del contenido de dichos archivos, más no indica que puedan presentar otros nombres/a>

# Actualizaciones Tarea

> 30 de agosto
1. Se hace un cambio menor en el enunciado, en la sección __4.1 Jardín__, en Inventario Plantas se reemplaza la palabra __compradas__ por __que llegan__ y en la sección __5.4 Llegada de plantas__ se agrega que las plantas son __guardadas en el inventario__.
> 2 de septiembre
1. Se hace un cambio menor en el archivo __plantas.txt__ para que hayan 6 líneas erróneas. 
2. Se hace un cambio menor en el enunciado, se cambia ejemplo de archivo plantas.txt para que hayan 6 líneas erróneas. Además, se agregó explicación entrega atrasada.
> 6 de septiembre
1. Se hace un cambio menor en el enunciado, en la __Figura 11__ y __Figura 15__ la cantidad de solaretillos pasa de ser 3 a 4 para que estén de acorde con el tablero. 
> 9 de septiembre
1. Se hace un cambio menor en el enunciado, en la nota de pie 3 se agrega el nombre del jardín en el ejemplo.
