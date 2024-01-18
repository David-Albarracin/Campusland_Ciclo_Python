"""
Hacer un algoritmo que muestre el número intermedio de tres números ingresados

Hacer un programa que muestre el número intermedio de tres números enteros ingresados.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

n1 = reusable.inputNumber("INGRESE NÚMERO 01")
n2 = reusable.inputNumber("INGRESE NÚMERO 02")
n3 = reusable.inputNumber("INGRESE NÚMERO 03")

if (n1 > n2):
    medio = n1
    xtem = n2
else:
    medio = n2
    xtem = n1

if (medio > n3):
    medio = n3

if (medio < xtem):
    medio = xtem

print(f"EL NÚMERO MEDIO ES : {medio}")