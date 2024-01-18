"""
Hacer un algoritmo que muestre el factorial de un número ingresado
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable
promedio = 0

cuantasNotas = reusable.inputNumber(f"Ingresa la Cantidad de notas que quieres Ingresar")

for i in range(cuantasNotas):
    nota = reusable.inputNumber(f"Ingresa la Nota N°{i + 1}")
    promedio += nota 

print(f"El Promedio de las 3 Notas es {promedio / cuantasNotas}")