"""
Hacer un algoritmo que muestre el área y perímetro de un círculo

Hacer un programa para calcular el área y perímetro de un círculo.
ÁREA DEL CÍRCULO : AREA = PI * (r * r)
PERÍMETRO DEL CÍRCULO : PERÍMETRO = 2 * PI * r 
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


lado = reusable.inputFloat("LADO")

area =  lado * lado

print(f"AREA : {area}cm")


perimetro = 4 * lado

print(f"PERÍMETRO : {perimetro}cm")