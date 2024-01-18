"""
Se requiere realizar un programa en Python que permita leer 3 números enteros positivos e imprima
La sumatoria de los tres números.

"""

import os
#Variable para guardar los numeros
listNumbers  = []
#Variable acumulativa que ira guardando la suma de los numeros
suma = 0

#Ciclo Para obtener los si o si 3 Numeros Positivos
while (len(listNumbers) < 3):
    #Try para evitar errores de typo value
    try:
        numero = int(input("Ingresa un Numero Positivo :> "))
    except ValueError:
        print("Solo números enteros positivos")
    else:
        #Comprobacion si es positivo
        if (numero > 0):
            suma += numero
            listNumbers.append(numero)
        else:
            print("Solo números enteros positivos")


print(f"La Sumatoria Es : {suma}")