"""
HACER UN ALGORITMO QUE MUESTRE EL SUELDO DE UN TRABAJADOR 

Elaborar un algoritmo que permita ingresar el nombre del trabajador, 
sueldo básicos y el número de hijos, se debe mostrar su bonificación y el sueldo final. 
Tenga en cuenta que la empresa está dando una bonificación del 7% del sueldo básico, 
sólo en el caso de que el trabajador tuviese hijos.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

boni = 0
sueldoF = 0

nom = input("Ingrese Nombre")
sueldoB = reusable.inputNumber("Sueldo Básico")
hijos = reusable.inputNumber("Numeroo de Hijos")

if (hijos > 0):
    boni = sueldoB * 0.7

sueldoF = sueldoB + boni

print(f"BONIFICACIÓN : S/.{boni}")
print(f"SUELDO FINAL : S/.{sueldoF}")
