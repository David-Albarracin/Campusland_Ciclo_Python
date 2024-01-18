"""
Algoritmo que genere 10 números aleatorios que estén en el rango de 10 a 99 
"""

import random



listNumber = []

for i in range(10):
    listNumber.append(random.randint(10, 99))

print(listNumber)