"""
Hacer un algoritmo que imprima los 10 primeros números pares
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

numero = 1
listNumbers = []

while(len(listNumbers) < 10):
    numero += 1
    if ((numero % 2) == 0 ):
        listNumbers.append(numero)

print(listNumbers)