"""
Algoritmo que ingrese un total de segundos y muestre cuantas horas, minutos y segundos hay.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable
import math

segundos = reusable.inputNumber("Ingresa el numero de segundos")

hor = math.trunc(segundos / 3600)
min = math.trunc((segundos - (hor * 3600)) / 60)
seg = math.trunc(segundos - ((hor * 3600) + (min * 60)))

print(f"HORAS : {hor}")
print(f"MINUTOS : {min}")
print(f"SEGUNDOS : {seg}")

