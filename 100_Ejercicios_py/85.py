"""
Hacer un algoritmo que muestre si un número es positivo o negativo

Hacer un programa dónde se ingrese un número entero y muestre si es un número positivo o negativo, 
considerar 0 como positivo.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

num = reusable.inputFloat("INGRESE NÚMERO" )

if (num >= 0):
    print(f"NÚMERO POSITIVO")
else:
    print(f"NÚMERO NEGATIVO")