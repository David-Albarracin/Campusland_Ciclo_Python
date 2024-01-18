"""
Hacer un algoritmo que muestre el área y perímetro de un pentágono

Hacer un programa que calcule el área y el perímetro de un pentágono.
ÁREA DEL PENTÁGONO : ÁREA = (P * ap)/2
PERÍMETRO DEL PENTÁGONO : PERÍMETRO = 5L
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

base = reusable.inputFloat("BASE EN CM")
altura = reusable.inputFloat("ALTURA EN CM")

area =  base * altura

print(f"ÁREA : {area}cm")


perimetro = (2 * altura) + (2 * base)

print(f"PERÍMETRO : {perimetro}cm")