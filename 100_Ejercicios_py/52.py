"""
Hacer un algoritmo que muestra el área y perímetro de un trapecio

Hacer un programa que muestre el área y perímetro de un trapecio.
ÁREA DEL TRAPECIO : ÁREA = ((B + b) * h) / 2
PERÍMETRO DEL TRAPECIO : PERÍMETRO = B + b + L1 + L2
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


baseMayor = reusable.inputFloat("BASE MAYOR EN CM")
baseMenor = reusable.inputFloat("BASE MENOR EN CM")
altura = reusable.inputFloat("ALTURA EN CM")


area =  ((baseMayor * baseMenor) * altura) / 2

print(f"ÁREA : {area}cm")


laso_1 = reusable.inputFloat("LASO 01 EN CM")
laso_2 = reusable.inputFloat("LASO 02 EN CM")
laso_3 = reusable.inputFloat("LASO 03 EN CM")
laso_4 = reusable.inputFloat("LASO 04 EN CM")


perimetro = laso_1 + laso_1 + laso_1 + laso_1

print(f"PERÍMETRO : {perimetro}cm")