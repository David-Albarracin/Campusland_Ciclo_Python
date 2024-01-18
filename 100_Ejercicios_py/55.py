"""
HACER UN ALGORITMO PARA CONVERTIR DE GRADOS FAHRENHEIT A CELSIUS 
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


fahrenheit = reusable.inputFloat("Temperatura Fahrenheit")

celsius = (fahrenheit - 32) * (5 / 9)

print(f"CELSIUS : {celsius}")