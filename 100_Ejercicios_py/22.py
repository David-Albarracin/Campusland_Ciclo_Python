"""
Hacer un algoritmo que imprima los 10 primeros números impares
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

numero = 1
listNumbers = []

while(len(listNumbers) < 10):
    if ((numero % 2) != 0 ):
        listNumbers.append(numero)
    numero += 1

print(listNumbers)