"""
Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.

a. Total de números ingresados
b. Total de números pares ingresados
c. Promedio de los números pares
d. Promedio de los números impares
e. Cuantos números son menores que 10
f. Cuantos números están entre 20 y 50
g. Cuantos números son mayores que 100

"""
import os
#Variables para Guardar todos los numeros Ingresados y contadores para pares y menores que 100 y ...
listNumbers = []
pares = 0
menor_10 = 0
entre_20_50 = 0
mayor_100 = 0

#Ciclo que se mantiene en ejecucion Mientras Numero Sea > 0
while(True):
    try:
        os.system("cls")
        numero = int(input("Ingresa un Numero Entero o (-1 Para Salir) :> "))
    except ValueError:
        print("Ingresa solo Numeros")
    else:
        if (numero <= 0):
            #Optenemos la Cantidad de Numeros Ingresados
            cantidadNumeros = len(listNumbers)
            #Mostramos en pantalla los Datos Requeridos
            print(f"Total de números ingresados es : {cantidadNumeros}")
            print(f"Total de números pares ingresados es : {pares}")
            promedio = (pares / cantidadNumeros) * 100
            print(f"El {promedio}% son Numeros Pares")
            print(f"El {(100 - promedio)}% Son Numeros Impares")
            print(f"{menor_10}    números son menores que 10")
            print(f"{entre_20_50}    números están entre 20 y 50 ")
            print(f"{mayor_100}    números son mayores que 100")
            break
        else:
            #Bloque de codigo que nos ayuda a sumar pares y numeros mayores que 100
            if((numero % 2) == 0):
                pares += 1
            if(numero > 100):
                mayor_100 += 1
            elif((numero < 10)):
                menor_10 += 1
            elif(numero >= 20) and (numero <= 50):
                entre_20_50 += 1
            #--fin del bloque de codigo
            #Mostrar en Pantalla un mensaje al Usuario que todo Salio Bien
            print("Numero Ingresado Correctamente")
            listNumbers.append(numero)
            os.system("pause")
    