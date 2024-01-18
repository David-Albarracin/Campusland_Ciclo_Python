"""
Hacer un algoritmo para calcular el área y perímetro de un cuadrado 

Hacer un programa que muestre el área y perímetro de un cuadrado.
ÁREA DEL CUADRADO : AREA = L * L
PERÍMETRO DEL CUADRADO : PERÍMETRO = 4 * L
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


lado = reusable.inputFloat("LADO EN CM")

area = lado * lado
perimetro = 4 * lado

print(f"AREA : {area}cm")
print(f"PERIMETRO : {perimetro}cm")