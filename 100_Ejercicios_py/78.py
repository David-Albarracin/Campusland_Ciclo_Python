"""
Algoritmo que muestre si una persona es mayor o menor de edad, según la edad ingresada.

Hacer un programa que permita ingresar una determinada edad y muestre si es mayor o menor de edad, 
considere 18 en adelante como mayor de edad.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

edad = reusable.inputNumber("INGRESE EDAD")

if (edad >= 18):
    print(f"ES MAYOR DE EDAD")
else:
    print(f"ES MENOR DE EDAD")