"""
ALGORITMO QUE MUESTRA EL TRIÁNGULO DE PASCAL
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

M = []

numero = reusable.inputNumber("INGRESE DIMENSIÓN [MENOS O IGUAL A 20]")

for IZQ in range(numero):
    M.append([])
    M[IZQ].append(1)
    for DER in range(1, IZQ):
        M[IZQ].append(M[IZQ - 1][DER - 1] + M[IZQ - 1][DER])
    if (numero != 0):
        M[IZQ].append(1)

for IZQ in range(numero):
    print(" " * (numero - IZQ), end = "")
    for DER in range(0, IZQ + 1):
        print("{0:2}".format(M[IZQ][DER]), end = "")
    print()