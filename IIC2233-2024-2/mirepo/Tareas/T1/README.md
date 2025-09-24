# Tarea 1: DCCultivo 🌱💧


## Consideraciones Generales:
El programa puede crear un plano, plantar en ese plano, eliminar cultivos, más no puede regar, puede crear predios  más no regar como se solicita esos predios, no puede detectar plagas tampoco, el menu funciona en su totalidad, sin embargo, es necesario comentar u omitir la funcion DCCultivo.buscar_y_regar, dado que al seguir las indicaciones del menu pero ingresando valores no ideales, o que necesiten cambiar de predio, dará error por culpa de esa funcion.

### Cosas implementadas y no implementadas

#### Automatización: 36 pts (60%)
##### ✅ Predio: crear_plano
En este ítem, se escribieron dos sentencias **"if"** para realizar las acciones de crear un plano normal y crear un plano de riego,
luego, dentro de cada sentencia se abrió un ciclo "for" con el alto solicitado como rango, esto para que cada repetición formara una fila,
dentro de este ciclo **“for”** se creó una lista vacía, donde se añadirían los elementos solicitados, que representan las columnas, esto se hizo
abriendo otro ciclo **"for"** para añadir los elementos de la fila, pues su rango es el ancho entregado, finalmente se añade esta nueva fila a
la **lista de listas** que representaba el plano, este ciclo se repite según cuan alto se desea el plano.
##### ✅ Predio: plantar
En este ítem primero se separan las coordenadas y se nombran como inicio filas e inicio columnas, luego se crea un **”bool”** que señalará más tarde la disponibilidad del espacio para plantar, se inicia un ciclo **”for”** para revisar fila por fila, dentro de este se inicia otro ciclo **”for”** correspondiente a las columnas, representadas por los elementos dentro de la fila, luego se verifica por medio de un condicional if que no se sobrepasen los límites de la lista para evitar un error, si todo está en orden continua al siguiente condicional if, el cual verifica que el espacio esté disponible, si tan solo uno de los espacios no está disponible, se cambia el **”bool”** disponibilidad a False, luego se revisa el **”bool”** disponibilidad para verificar si se puede plantar según los requerimientos, si la respuesta es afirmativa, se realizan ciclos **”for”** analógicos pero para ir reemplazando cada “X” por el código de cultivo correspondiente. 
##### 🟠 Predio: regar
En este ítem se separan las coordenadas como centros de las filas y columnas, luego se asignan **”variables”** de fila superior e inferior y columna inicial y final, esto para diferenciarlas de las demás dado que según el funcionamiento solicitado, los bordes no deben ser regados, luego se inicia un **”for”** en el rango del tamaño del circulo a regar, donde se declaran condicionales **”if”** y **”elif”** para distinguir entre los bordes y el resto del círculo, esto comparando las **”variables”** que modifica el **”for”** con las **”variables”** establecidas como fila superior e inferior, si se encuentra una de estas, se declara un **”for”** para regar esta zona evitando los bordes, utilizando un rango especifico que omite el primer elemento y el ultimo de esa fila, el segundo condicional **”elif”** realiza un proceso análogo pero regando toda la fila.
##### ✅ Predio: eliminar_cultivo
En este ítem se crea un contador para las celdas eliminadas, luego se crea un ciclo **"for"** para recorrer cada fila del predio, dentro se crea otro ciclo **"for"** para recorrer cada elemento de la fila, aquí se verifica si la ubicación actual en el plano según los **"ciclos"** contiene un cultivo que se desea eliminar, si la respuesta es afirmativa, **"reemplaza"** ese elemento por un “X” y suma uno al contador de celdas eliminadas, finalmente **"retorna"** ese contador.
##### ✅ DCCultivo: crear_predios
En esta función primero se crea un **”string”** que añade el prefijo “data/” al nombre del archivo entregado para luego verificar si existe aquel archivo, si la respuesta es afirmativa, lo abre con **”with”** y guarda todo su contenido en una lista, luego se ejecuta un ciclo **”for”** por elemento de esa lista, para **”quitarles”** el carácter salto de linea y separar su contenido que viene en formato **”código_predio,alto,ancho”** para luego crear una **”instancia de Predio”** con estos elementos, dentro de esta instancia se crean los dos tipos de plano correspondientes, y se añaden a la lista de predios de la **”instancia de DCCultivo”**, para finalmente **”retornar”** el **“string”** correspondiente de carga exitosa, en caso que el archivo no exista, **”retorna”** en su lugar el **”string”** correspondiente al fallo.
##### 🟠 DCCultivo: buscar_y_regar
En esta función se asignan las variables para totalidad del espacio disponible, inicio columnas e inicio filas, junto con un **“bool”** que indica si se logra plantar o no, luego se hace un ciclo **”for”** que recorra los elementos de la lista de predios, dentro, se crea un **”bool”** para indicar si se puede plantar en el predio actual, luego se llama a la **”función plantar”** del predio actual para intentar plantar, se crea una variable que indica el área total a plantar, para después, recorrer el área dentro del plano del predio actual por medio de ciclos **”for”** que recorren las filas y cada elemento dentro de ellas, **“sumando uno”** a la variable de espacio disponible si se encuentra el código de cultivo que se deseaba plantar, si esta variable coincide con el área total a plantar, si coinciden, retorna un **“bool”** True.
##### ❌ DCCultivo: detectar_plagas


#### Menú: 13 pts (21,7%)
##### ✅ Consola
Se crea un **“while”** que sirve de **“loop”** para volver al menú principal cada vez que se necesite.
##### ✅ Menú de Inicio
Se imprime en pantalla un “menú” que indica las opciones disponibles, además de dar al usuario el input correspondiente, se crean condicionales **“if”** para las dos opciones, crear predios y cerrar el programa, además de un **”else”** por si se escribe algo además de las dos opciones, si se elige la opción 1, se ingresa al menú de acciones.
##### ✅ Menú de Acciones
Si se presiona la opción 1, se le pide al usuario escribir el nombre del archivo para cargar los predios, luego se crea una instancia de DCCultivo y se crea una variable que almacene lo retornado por crear predios con el nombre del archivo en la instancia, si esta variable coincide con el string de fallo de la función crear predios, retorna un mensaje informando al usuario, caso contrario, se abre un nuevo loop con las opciones dentro de ese predio.

##### Aspectos_Generales: 7 pts (11,7%)
##### ✅ Modularización
Se verificó que ningún archivo superara las 400 líneas.
##### ✅ PEP8
Se agregaron espacios entre operadores, después de cada “,” y se verificó que cada línea fuera de 100 caracteres o menos.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```data/``` en ```misma carpeta de main.py```
2. ```predios.txt``` en ```data``` (este archivo puede tener otro nombr, pero debe estar en data/)

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path.exists```
2. ```sys```: ```exit``` 

### Librerías propias
No se han creado librerias propias, solo se utilizan los archivos base

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <La carpeta data existirá en el mismo directorio que main.py y dccultivo.py, con ese nombre y contendrá un archivo .txt, es valido ya que en el enunciado se indica que lo que puede cambiar es el archivo predios.txt, manteniendo el formato, más no se indica que la carpeta pueda cambiar de nombre, o que sea posible abrir un archivo en el directorio de dccultivo.py ademas del subdirectorio data/a> 
# Actualizaciones Tarea

> 13 de agosto

1. Se sube la tarea al repositorio Syllabus.
2. Se cambia y actualiza el Enunciado ya que se añadía una extensión .py innecesaria para el comando de ejecución de _tests_. Específicamente en la sección 6.1 Ejecución de _tests_.

    En cambio, si deseas ejecutar un subconjunto de _tests_, puedes hacerlo escribiendo lo siguiente:

    `python3 -m unittest -v -b tests_publicos.<test_N>`

    Reemplazando `<test_N>` por el test que desees probar

    Por ejemplo, si quisieras probar si realizaste correctamente el método crear_plano de Predio, deberás escribir lo siguiente:

    `python3 -m unittest -v -b tests_publicos.test_00_crear_plano`

> 19 de agosto

1. Se hace un cambio menor al enunciado, en la subsección __3.2.2 Menu de Acciones__. Para la acción Plantar del menú, se mencionaba ingresar `codigo_cultivo` como _str_, cuando es indiferente el tipo de dato ya que todos los datos ingresados con input() entran como _str_. Se precisa esto para eliminar confusiones en el enunciado de la siguiente forma:
    > Plantar: (...)Puedes asumir que el usuario ingresará correctamente los datos, es decir, entregará un número entero válido entre 0 y 9 para el parámetro de `codigo_cultivo` y dos números enteros positivos para los parámetros de `alto` y `ancho`. (...)