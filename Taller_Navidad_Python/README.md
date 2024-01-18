
![Logo](https://www.python.org/static/img/python-logo.png)



# Taller Practico Navideño 

Este taller está diseñado con pautas específicas que facilitarán la comprensión del código contenido en los archivos.



## Pautas Generales


1. **Estructura de Carpetas:**
    El proyecto está organizado en carpetas con nombres relacionados a taller y los 100 ejercicios.

      - **[100 EJERCICIOS](https://github.com/David-Albarracin/TallerNavidenoPython/tree/main/100_Ejercicios_py).**
         Contiene 100 ejercicios en Python, numerados del 1.py al 100.py tambien Incluye un archivo [reusable.py](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/100_Ejercicios_py/reusable.py) que alberga funciones reutilizadas en varios ejercicios. Cada ejercicio (n.py) incluirá un comentario explicativo del problema a solucionar.

      - **[NIVEL PRINCIPIANTE](https://github.com/David-Albarracin/TallerNavidenoPython/tree/main/Nivel_Principiante).**
        Contiene los 3 ejercicios del taller de navidad de nivel principiante. El análisis de cada ejercicio proporcionará una explicación concisa de cómo se resolvió.

      - **[NIVEL INTERMEDIO](https://github.com/David-Albarracin/TallerNavidenoPython/tree/main/Nivel_Intermedio).**
         Incluye los 3 subcarpetas que tienen como nombre ejercicio 1, ejercicio 2, ejercicio 3 del taller de navidad de nivel intermedio. Cada ejercicio, detallado en la sección de análisis, presenta una explicación de su solución los 3 estan modulados y para testearlos se requiere ejecutar el main.py.

      - **[NIVEL EXPERTO](https://github.com/David-Albarracin/TallerNavidenoPython/tree/main/Nivel_Experto).**
         Contiene el único ejercicio del taller de navidad de nivel experto, organizado en módulos. Para probar este ejercicio, se debe ejecutar el archivo main.py.

      - **[NIVEL AVANZADO](https://github.com/David-Albarracin/TallerNavidenoPython/tree/main/Nivel_Avanzado).**
         Similar a la carpeta de Nivel Experto, contiene el único ejercicio de nivel avanzado dividido en módulos. La ejecución exitosa implica ejecutar el archivo main.py.

3. **Variables Comentadas:**
    Algunas variable contiene un comentario descriptivo justo encima de ella para proporcionar información sobre el tipo de datos que almacena.

4. **Funciones Documentadas:**
    Algunas funciones incluyen comentarios que explican el proceso que llevan a cabo. Estos comentarios proporcionan detalles sobre la funcionalidad de la función y el valor que se espera que retorne.

5. **Analisis**
    Algununos analisis tienen lijeros cambios al momento de ver en codigo 

## Contribuciones

Estas prácticas estructuradas y documentadas facilitarán la comprensión y colaboración en el desarrollo de software, siguiendo las mejores prácticas de la comunidad de desarrollo; Si desea Mas Informacion relacionados con los 100 ejercicios lo invito a visitar [100 EJERCICIOS PSEING](https://www.youtube.com/watch?v=3CNVzw4Kee0&list=PLtzBCV-VcS_TsqlBrmWoq_f0MR7WIpJS9&index=1).

# Análisis:

## Nivel Principiante:

- **[Ejercicio 1](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/Nivel_Principiante/Ejercicio_1.py).**

   - **Descripción del Problema:**
      Se requiere realizar un programa en Python que permita leer 3 números enteros positivos e imprima la sumatoria de los tres números.

   - **Solución Propuesta:**
      Para abordar esta problemática, comenzamos declarando tres variables destinadas a almacenar el número ingresado, la lista de números y la suma de estos. Con el fin de gestionar posibles errores y asegurar la entrada de números positivos únicamente, incorporaremos un bucle while que permanecerá en ejecución hasta que tengamos los tres números requeridos. Estos números se almacenarán en la variable "numeros", la cual se convertirá explícitamente a tipo entero. A continuación, se verificará si el número es positivo y se guardará en la lista "listNumbers". Posteriormente, se sumará a la variable "suma" una vez confirmada su positividad.
      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |numero|Entrada|int()|
      |listNumbers|Salida|list()|
      |suma|Salida|int()|


- **[Ejercicio 2](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/Nivel_Principiante/Ejercicio_2.py).**

   - **Descripción del Problema:**
      El Centro de Salud de Campuslands busca desarrollar un programa para calcular el Índice de Masa Corporal (IMC) de 20 estudiantes nuevos. El programa deberá mostrar el nombre del estudiante, la edad, el IMC y la categoría correspondiente. Además, se requiere generar un informe con pautas indicadas

   - **Solución Propuesta:**
      Para abordar esta problemática, comenzamos generando un ciclo que requiera el registro de 20 estudiantes luego le pediremos al usuario que ingrese los datos segun la estructura del estudiante que nos ayudara a almacenar los datos
      ```python
      estudiante = {
         "nombre": nombre,
         "edad": f"{edad} Años",
         "peso": f"{peso} Kg",
         "altura": f"{altura} Mts",
         "imc": imc,
         "rango": imcRango
      }
      ```
      Luego de Pedirle los datos necesarios generaremos el valor de imc = peso / (altura * altura) y llamaremos a la funcion getRango_IMC(imc) esta nos retorna el rango en el que se encuentra el estudiante dependiendo de su imc como Peso Ideal, Sobre peso .....

      Teniendo Estos Datos Generamos en pantalla un informe con los datos requeridos
      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |reporte|Salida|dict()|
      |estudiantes|Salida|list()|
      |estudiante|Salida|dict()|
      |imc|Salida|float()|

- **[Ejercicio 3](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/Nivel_Principiante/Ejercicio_3.py).**

   - **Descripción del Problema:**
      Se busca crear un programa en Python que permita ingresar una cantidad n de números enteros positivos. Cuando se introduce un número negativo, el programa mostrará un informe con pautas expecificas

   - **Solución Propuesta:**
      Para abordar esta problemática, comenzamos asignando un espacio en memoria donde se almacenarán los numeros ingresados, cuantos numeros pares, cuantos menores que 10, cuantos entre 20 y 50 y cuantos mayor que 50 luego luego como no sabemos la cantidad de numeros crearemos un ciclo que finalize cuando el usuario ingrese un numero negativo, cuando el usuario ingrese un numero lo pasaremos por un trozo de codigo que nos ayudara a determinar en que espacio de memoria se guardara teniendo en cuenta las pautas anteriores luego se mostrara en pantalla un resumen del informe
      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |listNumbers|Entrada|list()|
      |pares|Salida|int()|
      |menor_10|Salida|int()|
      |entre_20_50|Salida|int()|
      |mayor_100|Salida|int()|
## Nivel Intermedio:

- **[Ejercicio 1](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/Nivel_Intermedio/Ejercicio_1/main.py).**

   - **Descripción del Problema:**
      El centro de prevención de sismos en Colombia desea realizar un programa que le permita llevar el Registro del los sismos presentados en 5 ciudades del país. Por cada ciudad se realizan n cantidad de Registros. El programa debe permitir registrar las muestras del movimiento en cada ciudad.

   - **Solución Propuesta:**
        Para abordar esta problemática, comenzaremos creando una lista llamada "ciudades" que servirá para almacenar la información de las ciudades que creemos en la opción 1 del menú. Dado que solo podemos utilizar listas, la estructura de cada ciudad también será una lista. En la posición 1 de la lista estará el nombre de la ciudad, en la posición 2 estarán los sismos registrados en esa ciudad, y en la posición 3 estará el porcentaje de incidencia de sismos en dicha ciudad.
        ```python
        ciudades.append([uid,nombre,[],0.0])
        ```
        para la opcion de registrar sismos primero le pediremos a el usuario que ingrese la ciudad a registar el sismo luego buscaremos el nombre que consida con el dato ingresado del usuario y luego le pediremos que ingrese el sismo y comprobamos que el numero de sismos concidan con la cantidad de las otras ciudades si no es haci el usuario tendra que ingresar los datos para las otras ciudades
      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |ciudades|Entrada|list()|
      |ciudad|Entrada|list()|
      |opcion|Entrada|str()|


- **[Ejercicio 2](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/Nivel_Intermedio/Ejercicio_2/main.py).**

   - **Descripción del Problema:**
      La alcaldía de Bucaramanga desea realizar un programa que le permita calcular el valor de CO2 producido En las diferentes instalaciones gubernamentales de la ciudad.

   - **Solución Propuesta:**
      Para abordar esta problemática, inicialmente, mostraremos en pantalla el menú principal, incluyendo la opción de registrar dependencia. Una vez que la dependencia esté registrada, procederemos a agregar el consumo correspondiente para cada dependencia. Para ello, se implementará un formulario que constará de las siguientes preguntas:
        ¿Cuántos computadores tiene la oficina? ¿Cuenta la oficina con horno microondas? ¿La oficina dispone de mensajeros que utilizan el carro o la moto de la empresa? En caso afirmativo, ¿cuántos kilómetros aproximados recorren estos mensajeros? ¿Cuántos televisores tiene la oficina? Este formulario nos permitirá recopilar información detallada sobre el consumo de recursos en cada dependencia, contribuyendo así a un análisis más preciso y eficiente de los consumos energéticos y logísticos de la empresa 
        ```python
        #estas son de las formulas para allar el CO2
        #El caso del Trasporte dividimos los quilometros por 30 para obtener cuantos galones se consumieron y lo multiplicamos por 3.7 para obtener los litros y el factor de emision de la gasolina es de 2,31 kg de CO2 por litro consumido
        Emisiones de CO2 (Transporte) = ((kilómetros Recorridos / 30 )*3.7) * 0.023
        
        #Para los Electrodomesticos se usa

        Consumo del Dispositivo = ((nPotencia * 8) / 1000) * 30

        #Para la Luz

        Emisiones de CO2 (Electricidad) = (suma Dispositivos) * (factor de emicion)

        ```
        Luego estos datos los alamacenamos en la lista de dependencias con sus respectivos valores y esto lo usamos para poder mostrar el consumo de co2 de cada dependencia y la dependencia con mayor consumo
        

      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |departamentos|Entrada|list()|
      |departamento |Entrada|dist()|
      |factor_electricidad|Salida|float()|


- **[Ejercicio 3](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/Nivel_Intermedio/Ejercicio_3/main.py).**

   - **Descripción del Problema:**
      En el contexto de la gestión de inventarios, se requiere desarrollar un programa en Python que permita realizar el control detallado de productos en un negocio.

   - **Solución Propuesta:**
        Para dar solucion,primero mostraremos en pantalla un menu que tenga la opcion Regitrar producto esta opcion pedira los datos del producto como su nombre su codigo su valor de compra el valor de venta ... el la opcion 2 del menu contamos con ver lista de productos que nos mostrara una lista de todos los productos con sus datos claro mensionados anterior mente la opcion 3 contara con el apartado actualizar stock que nos permitira cambiar el stock del producto la opcion 4 nos ayudara a ver una lista de los productos que se encuentran en estado critico y el stock esta por los limites permitidos la opcion de calculo de nPotencia nos ayudara a mostrar una lista ordena del producto mas rentable al menos rentable 
        ```python
        #Estructura del Producto

        producto = {
            "codigo": "123"
            "nombre": ""
            "stock": 0
            "valor_de_compra": 0
            "valor_de_venta": 0
            "stock_minimo": 0
            "stock_maximo": 0
            "nombre_del_provedor": ""
            "ganancia": 0
        }
        
        ```
      
      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |productos|Salida|dist()|
      |producto |Salida|dist()|
      |stock|Entrada|int()|
      |operation|Entrada|int()|

## Nivel Avanzado:

- **[Torneo de tenis de mesa](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/Nivel_Avanzado/main.py).**

   - **Descripción del Problema:**
      El departamento de bienestar de campus desea organizar un torneo de tenis de mesa y requiere Un programa que le permita llevar el control de los juegos llevados a cabo por cada uno de los Inscritos en el torneo. El programa debe cumplir con unos requerimientos

   - **Solución Propuesta:**
        Para abordar esta problemática, se comenzará con la creación de un menú que incluirá la opción de registrar un nuevo camper. El programa solicitará información como el nombre y la edad, y, en función de la edad, asignará automáticamente una categoría al camper. Se llevará un registro detallado de cada jugador, incluyendo partidas jugadas, partidas ganadas, partidas perdidas, puntos a favor y el total de puntos. La estructura del camper se visualiza de la siguiente forma:
        ```python
        camper = {
            "id": "Generado aleatoriamente",
            "nombre": "Nombre del camper",
            "edad": 12,
            "PJ": "Partidas Jugadas",
            "PG": "Partidas Ganadas",
            "PP": "Partidas Perdidas",
            "PA": "Puntos a Favor",
            "TP": "Total de Puntos"
        }
        ```
        Una vez que haya al menos cinco participantes en cada categoría, se habilitará la opción de jugar partidos. En esta opción, se generarán números aleatorios para determinar el ganador, siendo aquel con el número más alto. Los resultados de cada partida se guardarán y se actualizarán los estadísticas del camper correspondiente.
      
      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |novatos|Entrada|list()|
      |intermedio|Entrada|list()|
      |avanzado|Entrada|list()|
      |camper|Salida|dist()|
      |opcion|Entrada|str()|
## Nivel Experto:

- **[Seguimiento Académico de todos los campers](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/Nivel_Experto/main.py).**

   - **Descripción del Problema:**
      El departamento académico de campuslands desea crear un programa que le permita llevar el seguimiento Académico de todos los campers que se encuentran matriculados en el programa intensivo de programación el programa tiene unas pautas requeridas.

   - **Solución Propuesta:**
      Para abordar esta problemática, comenzamos abordando las pautas requeridas y dandoles solucion una a una
      - **Registro de campers**:
         Para este punto, crearemos una opción en nuestro menú principal denominada "1. Registrar Camper". Esta opción estará vinculada a una función que solicitará los datos necesarios, asegurándose de la integridad de los mismos. La estructura del camper será la siguiente:
         ```python
         camper = {
            "uid": "cedula de ciudadanida / targeta de identidad",
            "codigo": "un numero random de 0000",
            "nombre": "Nombre del camper",
            "apellidos": "Apellidos del camper",
            "ciudad": "bucaramanga" <- Predefinido
            "direccion": "Direccion de recidencia en bucaramanga",
            "acudiente": "Persona a contactar en caso de emergencia",
            "telefono": {
               "celular:" "999-999-9999"
               "fijo": "000-777-7777"
            }	,
            "estado": "",
            #Explicacion de la ruta en el apartado Ruta
            "ruta": {
               "uid": "",
               "trainer": "",
               "area": "",
               "jornada": ""
               "moduloFundamentos": {
                  "notaPruebaTecnica": "", 
                  "notaPruebaTeorica": "",
                  "notasTrabajosQuizes": ""
                  "definitiva": "(nT + nP + nTQ)"
               }
               "moduloWEB":{} as moduloFundamentos
               "moduloFormal": {} as moduloFundamentos
               "moduloBaseDatos" {} as moduloFundamentos
               "backend": {} as moduloFundamentos
            }
         }
         ```
      - **Registro de prueba**:
         En el menú principal, se añadirá otra opción para registrar los resultados de la prueba final. Esta opción solicitará la cédula del camper, y se introducirán las calificaciones de la PRUEBA PRÁCTICA y PRUEBA TEÓRICA. Si el promedio de estas calificaciones es igual o mayor a 60, se cambiará el estado del camper a "APROBADO"; de lo contrario, se establecerá como "NO APROBADO".
         ```python
            uid = input("Ingresa C.C. del Camper a Registar las notas")
            #camper = buscamos al camper en la base de datos por el uid
            notaPractica = input("Ingresa la Nota de la Prueba Practica")
            notaTeorica = input("Ingresa la Nota de la Prueba Teorica")
            #Se calcula el promedio promedio = (notaPractica + notaTeorica) / 2
            if (promedio >= 60):
               camper["estado"] = "APROBADO"
            else:
               camper["estado"] = "APROBADO"
         ```
      - **Registro de áreas de entrenamiento**:
         Las Áreas de Entrenamiento están compuestas por tres secciones: APOLO, SPUTNIK y ARTEMIS, cada una con un límite máximo de 33 campers. La estructura de estas áreas se visualiza de la siguiente manera:
         ```python
            areas = {
               "artemis":{
                  "trainer": "",
                  "ruta": "",
                  "fechaInicio": "",
                  "fechaFinal": "",
                  "campers":[] maxLen(33)
                  "jornada": ""
               }
            "sputnik": {} as artemis
            "apolo": {} as artemis 
            }
         ```
      - **Registro de áreas de entrenamiento**:
         Creación de Rutas de Entrenamiento: En el menú principal, se incluirá una opción para la creación de rutas. La secuencia de esta opción se presentará de la siguiente manera: Se solicitará al usuario ingresar el nombre de la ruta que se va a crear. Por cada módulo, se pedirá que añada los dos temas que se abordarán. Por ejemplo, "Fundamentos de Programación" podría tener como temas "Python" y "Pseing". Después de cada módulo, se imprimirá un mensaje en pantalla preguntando si desea continuar creando más módulos para la misma ruta.
         ```python
            rutas = {
               "nombreRuta": {
                  "fundamentosProgramacion": ["python", ""]
                  "programacionWEB": []
                  "programacionFormal": []
                  "basesDatos": []
                  "backend": []
               }

            }
            * Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
            * Programación Web (HTML, CSS y Bootstrap)
            * Programación formal (Java, JavaScript, C#)
            * Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.
            * Backend (NetCore, Spring Boot, NodeJS y Express)

         ```
      - **Gestor de Matrículas**
         En este proceso, comenzaremos solicitando el documento de identidad del camper, seguido de la especificación de la ruta asignada. Posteriormente, se registrarán las fechas de inicio y finalización de la matrícula. Este flujo de información facilitará la gestión eficiente de matrículas, asegurando un seguimiento adecuado del progreso de cada camper en su ruta de entrenamiento designada.
      
      - **Registro de Notas**
         En este módulo, iniciaremos solicitando el documento del camper. Con el documento proporcionado, procederemos a cargar las notas de manera secuencial. Por ejemplo, se comenzará con la nota correspondiente al primer tema del primer módulo de la ruta asignada. Este proceso se repetirá hasta completar la carga de todas las notas relacionadas con el desempeño del camper en su ruta de entrenamiento. La eficiente recopilación de esta información permitirá un seguimiento detallado del rendimiento académico de cada estudiante.
         ```python
         "moduloFundamentos": {
            "notaPruebaTecnica(nT)": input("Ingresa la nota") * 0.60, 
            "notaPruebaTeorica(nP)": "",
            "notasTrabajosQuizes(nTQ)": ""
            "definitiva": "(nT + nP + nTQ)"
         }
         ```
      - **Modulo de reportes**
         Módulo de Reportes: En esta sección se implementará un submenú con las siguientes opciones:

         a. Mostrar Campers Inscritos.

         b. Listar los campers que aprobaron el examen inicial.

         c. Listar los entrenadores que están trabajando con Campuslands.

         d. Listar los estudiantes que presentan bajo rendimiento

         e. Listar los campers y entrenador asociados a una ruta de entrenamiento.

         f. Mostrar la cantidad de campers que aprobaron y perdieron cada módulo, considerando la ruta de entrenamiento y el entrenador responsable.

         Este submenú proporcionará información clave para realizar un seguimiento detallado del desempeño de los campers, el trabajo de los entrenadores y la eficacia de las rutas de entrenamiento en Campuslands.

   - **Tabla de Declaración de Variables:**
      La Tabala contiene algunas funciones def() y solo contiene variables globales
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |camper|Entrada|dict()|
      |rutas|Entrada|dict()|
      |notaPractica |Entrada|int()|
      |notaTeorica  |Entrada|int()|
      |Areas  |Entrada|dict()|
      |moduloFundamentos  |Entrada|dict()|
      
