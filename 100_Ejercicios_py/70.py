"""
Algoritmo que muestre el promedio de 3 notas y muestre si esta aprobado o desaprobado.

Hacer un algoritmo que calcule el promedio de tres notas. 
Se puede tomar como referencia este ejercicio para promediar mas o menos notas.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

n1 = reusable.inputNumber("INGRESE NOTA 01")
n2 = reusable.inputNumber("INGRESE NOTA 02")
n3 = reusable.inputNumber("INGRESE NOTA 03")

prom = (n1 + n2 + n3)/3

if (prom > 10.5):
    print(f"APROBADO CON {prom}")
else:
    print(f"DESAPROBADO CON {prom}")