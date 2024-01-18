"""
HACER UN ALGORITMO PARA CALCULAR EL ÁREA Y PERÍMETRO DE UN PARALELOGRAMO

Hacer un programa que muestre el área y perímetro de un paralelogramo.
ÁREA DEL PARALELOGRAMO : ÁREA = B * h
PERÍMETRO DEL PARALELOGRAMO : PERÍMETRO = 2 x (b + h)
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


base = reusable.inputFloat("BASE")
altura = reusable.inputFloat("ALTURA")
area =  base * altura

print(f"ÁREA : {area}cm")

perimetro = (2 * altura) + (2 * base)

print(f"PERÍMETRO : {perimetro}cm")