"""
HACER UN ALGORITMO PARA CONVERTIR DE PULGADAS A PIES

Hacer un programa para convertir una longitud ingresada en pulgadas a pies.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

pul = reusable.inputFloat("INGRESE PULGADAS")

pies = (pul / 12)

print(f"PIES : {pies}")