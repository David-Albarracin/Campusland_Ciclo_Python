"""
Hacer un algoritmo que muestre el factorial de un número ingresado
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

fact = 1
numero = reusable.inputNumber("Ingresa el numero a calcular")

print(f"SERIE DEL FACTORIAL : ", end = "")
for x in range(1, numero + 1):
    print(f"{(numero + 1) - x} ", end = "")
    fact = fact * x

print(f"\nEL FACTORIAL ES : {fact}")