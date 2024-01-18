"""
HACER UN ALGORITMO QUE MUESTRA EL ÁREA Y PERÍMETRO DE UN PENTÁGONO

Hacer un programa que calcule el área y el perímetro de un pentágono.
ÁREA DEL PENTÁGONO : ÁREA = (P * ap)/2
PERÍMETRO DEL PENTÁGONO : PERÍMETRO = 5L
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


perimetro = reusable.inputFloat("PERÍMETRO EN CM")
apotema = reusable.inputFloat("APOTEMA EN CM")

area =  (perimetro * apotema) / 2

print(f"ÁREA : {area}cm")
lado = reusable.inputFloat("LADO EN CM")

perimetro = 5 * lado

print(f"PERÍMETRO : {perimetro}cm")