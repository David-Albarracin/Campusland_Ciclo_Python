"""
Hacer un algoritmo que ordene dos números ingresados

Hacer un programa que permita ingresar dos números y los muestre de forma ordenada de mayor a menor.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

n1 = reusable.inputNumber("INGRESE NÚMERO 01")
n2 = reusable.inputNumber("INGRESE NÚMERO 02")

if (n1 > n2):
    print(n1)
    print(n2)
else:
    print(n2)
    print(n1)