"""
Hacer un algoritmo que muestre una cantidad de dinero y en dólares y a euros
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


numero = reusable.inputNumber("Ingresa el Monto en COP")

print(f"DOLARES : {numero * 3800}")
print(f"EUROS : {numero * 4800}")