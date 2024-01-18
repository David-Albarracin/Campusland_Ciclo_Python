"""
Hacer un algoritmo que muestre el área y perímetro de un hexágono

Hacer un programa que muestre el área y perímetro de un hexágono.
ÁREA DEL PENTÁGONO : ÁREA = (P * ap)/2
PERÍMETRO DEL PENTÁGONO : PERÍMETRO = 6L
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable



perimetro = reusable.inputFloat("PERIMETRO")
apotema = reusable.inputFloat("APOTEMA")

area = (perimetro * apotema) / 2

print(f"AREA : {area}cm ")


lado = reusable.inputFloat("LADO")

perimetro = 6 * lado

print(f"PERIMETRO : {perimetro}cm")