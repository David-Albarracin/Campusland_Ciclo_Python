"""
Algoritmo que muestra todos los números que son capicúa de tres cifras en
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


listNumbers = []


for i in range(111, 999):
    numero = str(i)
    if (numero == (numero[::-1])):
        listNumbers.append(i)

print(listNumbers)