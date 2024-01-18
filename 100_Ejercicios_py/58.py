"""
HACER UN ALGORITMO PARA DISTRIBUIR EL PRESUPUESTO ANUAL DE UN HOSPITAL EN 3 ÁREAS.

Hacer un programa dónde el presupuesto anual de un hospital se distribuya en las siguientes áreas : 
Ginecología 40%, Traumatología 30% y Pediatría 30%, de un monto total de dinero asignado.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

presupuesto = reusable.inputFloat("INGRESE PRESUPUESTO")

ginecologia = presupuesto * 0.40
traumatologia = presupuesto * 0.30
pediatria = presupuesto * 0.30

print(f"Ginecología : ${ginecologia}")
print(f"Traumatología : ${traumatologia}")
print(f"Pediatría : ${pediatria}")