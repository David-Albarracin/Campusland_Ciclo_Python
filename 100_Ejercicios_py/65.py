"""
Hacer un algoritmo que muestre el área y volumen de un cilindro

Hacer un programa que calcule el área total de un cilindro y su volumen, 
ingresando el radio(r) y la altura(h) como datos de ingreso.
FORMULA : Para calcular el volumen de un cilindro; teniendo en cuenta la fórmula: V = π R2 * h.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable
import math

radio = reusable.inputFloat("RADIO")
altura = reusable.inputFloat("ALTURA")

area = 2 * math.pi * radio * (altura + radio)
volumen = math.pi * (radio * radio) * altura

print(f"ÁREA TOTAL DEL CILINDRO : {area}cm2")
print(f"VOLUMEN DEL CILINDRO : {volumen}cm3")

