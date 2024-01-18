"""
Hacer un algoritmo que muestre el área y perímetro de un triángulo 

Hacer un programa que muestre el área y perímetro de un triángulo.
ÁREA DEL TRIÁNGULO : A = (b * h) / 2; (Base por altura entre dos)
PERÍMETRO TRIÁNGULO EQUILÁTERO : P = L * 3; (La suma de cada uno de sus lados)
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable



base = reusable.inputFloat("BASE EN CM")
altura = reusable.inputFloat("ALTURA EN CM")

area = (base * altura) / 2

print(f"ÁREA : {area}cm")


lado = reusable.inputFloat("LADO EN CM")

perimetro = lado * 3


print(f"PERIMETRO : {perimetro}cm")