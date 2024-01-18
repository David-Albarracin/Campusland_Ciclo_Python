
"""
Hacer un algoritmo que muestre una serie gráfica de números del 9 al 1 en forma triangular
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

lista = []

for x in range(9):
    x += 1
    for i in range(10-x):
        lista.append(10-x)

    print(lista)
    lista = []