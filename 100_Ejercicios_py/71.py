"""
Hacer un algoritmo que muestre si un número es par o impar

Hacer un programa que permita ingresar un número entero y muestre el mensaje si es número par o número impar.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

num = reusable.inputNumber("INGRESE NÚMERO")

c = round(num / 2)
r = c * 2
re = num - r

if (re == 0):
    print(f"NÚMERO PAR")
else:
    print(f"NÚMERO IMPAR")