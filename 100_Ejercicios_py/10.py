"""
Hacer un algoritmo que muestre una cadena de texto 10 veces, usando ciclo repetitivo
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

listaPalabras = []

for x in range(1, 10):
    palabra = input(f"Palabra {x} : > ")
    listaPalabras.append(palabra)

print(listaPalabras)