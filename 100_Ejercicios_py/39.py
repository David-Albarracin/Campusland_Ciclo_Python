"""
Hacer un algoritmo que muestre el promedio de tres notas
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

totalNotas = 0

for i in range(3):
    nota = reusable.inputNumber(f"Ingresa la Nota N° {i + 1}")
    totalNotas += nota

print(f"El Promedio de las Tres Notas es : {totalNotas/3}")