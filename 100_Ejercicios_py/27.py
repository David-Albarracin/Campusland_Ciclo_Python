"""
Algoritmo que muestra los números primos desde 1 hasta N números ingresados
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


divisible = 0
numero = reusable.inputNumber("Ingresa un Numero")
listNumbers = ""

for cont in range(2, numero + 1):
    for divi in range(1, cont + 1):
        if ((cont % divi) == 0):
            divisible = divisible + 1
    if (divisible == 2):
        listNumbers += f"{cont} "
    divisible = 0
    
print(listNumbers)