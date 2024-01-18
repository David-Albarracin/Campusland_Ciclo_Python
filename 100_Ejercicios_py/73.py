"""
Hacer un algoritmo que calcule el costo de una llamada telefónica

Dado la duración (en minutos) de una llamada telefónica, 
calcular su costo, de la siguiente manera: Hasta 5 min el costo es 0.90. Por encima de 5 min el, 
costo es 0.90+0.20 por cada minuto adicional a los 5 primeros min.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

llamada = reusable.inputNumber("CANTIDAD DE MINUTOS")

if (llamada <= 5):
    costo = llamada * 0.9
else:
    costo = (5 * 0.9) + ((llamada - 5) * 1.1)

print(f"EL COSTO ES : ${costo}")