"""
El centro de salud de campuslands desea realizar un programa que le permita calcular el IMC de los
Estudiantes nuevos.

imc = peso(kg) / altura(m) al cuadrado

El programa debe mostrar el nombre del estudiante, la edad, el imc y la categoría según el IMC obtenido
Ver Imagen suministrada.

se requiere tener el registro de 20 estudiantes y poder determinar
el estado de salud de la comunidad estudiantil. El programa debe mostrar el siguiente reporte:}

a. Cuantos estudiantes se encuentran en el peso ideal.
b. Cuantos estudiantes se encuentran en obesidad grado I
c. Cuantos estudiantes se encuentran en obesidad grado II
d. Cuantos estudiantes se encuentran en obesidad grado III
e. Cuantos estudiantes se encuentran en Sobrepeso

"""
import os

#Funcion para obtener el rango del imc
def getRango_IMC(imc):
    if (imc > 10.8) and (imc < 24.9):
        #Contador de Estudiantes para peso ideal
        reporte["peso_ideal"] += 1
        #Retorna la categoria segun el imc
        return "Normal"
    
    elif (imc > 25) and (imc < 29.9):
        reporte["sobrepeso"] += 1
        return "Sobrepeso"
    
    elif(imc > 30) and (imc < 34.9):
        reporte["obesidad_grado_1"] += 1
        return "Obesidad 1"
    
    elif(imc > 35) and (imc < 39.9):
        reporte["obesidad_grado_2"] += 1
        return "Obesidad 2"
    
    elif(imc > 40):
        reporte["obesidad_grado_3"] += 1
        return "Obesidad 3"
#Diccionario donde se almacena el reporte de los estudiantes segun su IMC
reporte = {
    "peso_ideal": 0,
    "obesidad_grado_1": 0,
    "obesidad_grado_2": 0,
    "obesidad_grado_3": 0,
    "sobrepeso": 0
}

#Array Para Guardar los Estudiantes
estudiantes = []

#Ciclo para Pedir los 20 Estudiantes
for i in range(20):
    #Ciclo para evitar el ingreso de datos erroneos
    while(True):
        try:
            os.system("cls")
            nombre = input("Ingresa el Nombre del Estudiante :> ")
            edad = input(f"Ingrese la edad de {nombre} :> ")
            peso = float(input("Ingresa el Peso en KG :> "))
            altura = float(input("Ingresa la Altura en Metros :> "))
            imc = round(peso / (altura * altura), 1)
            imcRango = getRango_IMC(imc)
            estudiante = {
                "nombre": nombre,
                "edad": f"{edad} Años",
                "peso": f"{peso} Kg",
                "altura": f"{altura} Mts",
                "imc": imc,
                "rango": imcRango
            }
            #Mostrar en pantalla El primer estudiante ingresado
            os.system("cls")
            for key, value in (estudiante.items()):
                    print(f"{key.upper()} : {value}")

            estudiantes.append(estudiante)
            os.system("pause")
        except ValueError:
            print("Error Al Ingresar un dato")
            os.system("pause")
        else:
            break


    
os.system("pause")
os.system("cls")

#Punto 2
print(f"""
a. Se encuentran en el peso ideal {reporte['peso_ideal']} Estudiantes
b. Se encuentran en obesidad grado I {reporte['obesidad_grado_1']} Estudiantes
c. Se encuentran en obesidad grado II {reporte['obesidad_grado_2']} Estudiantes
d. Se encuentran en obesidad grado III {reporte['obesidad_grado_3']} Estudiantes
e. Se encuentran en Sobrepeso {reporte['sobrepeso']} Estudiantes
""")