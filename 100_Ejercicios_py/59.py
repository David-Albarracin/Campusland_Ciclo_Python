"""
HACER UN ALGORITMO QUE CALCULE EL ÁREA Y EL PERÍMETRO DE UN ROMBO

Hacer un programa que muestre el área y perímetro de un rombo.
ÁREA DEL ROMBO : AREA = (D * d) / 2
PERÍMETRO DEL ROMBO : PERÍMETRO = 4L
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable



diametroMayor = reusable.inputFloat("DIAMETRO MAYOR EN CM")
diametroMenor = reusable.inputFloat("DIAMETRO MENOR EN CM")

area =  (diametroMayor * diametroMenor) / 2

print(f"ÁREA : {area}cm")

lado = reusable.inputFloat("LADO EN CM")

perimetro = 4 * lado

print(f"PERÍMETRO : {perimetro}cm")