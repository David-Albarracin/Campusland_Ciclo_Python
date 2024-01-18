"""
Hacer un algoritmo que muestre la unidad, la decena y la centena 

Ingrese un número de tres cifras y mostrar su unidad, la decena y la centena.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

numero = 0


while (numero <= 100) and (numero <= 999):
    numero = reusable.inputNumber("Ingresa un Numero de Tres Cifras")

numero = str(numero)
print(f"CENTENA: {numero[0]}")
print(f"DECENA: {numero[1]}")
print(f"UNIDAD: {numero[2]}")