"""
ALGORITMO QUE MUESTRE EL COLOR MAS VOTADO
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

maxPersonas = reusable.inputNumber("INGRESA LA CANTIDAD DE PERSONAS")

rojo = 0
verde = 0
azul = 0
nulo = 0

for i in range(maxPersonas):
    color = input(f"PERSONA N°{i + 1} [ROJO - VERDE - AZUl] :> ").upper()
    if (color == "ROJO"):
        rojo += 1
    elif(color == "VERDE"):
        verde += 1
    elif(color == "AZUL"):
        azul += 1
    else:
        nulo += 1

if (rojo > verde) and (rojo > azul):
    print("EL ROJO FUE EL MAS VOTADO")
elif (verde > rojo) and (verde > azul):
    print("EL VERDE FUE EL MAS VOTADO")
elif (azul > rojo) and (azul > verde):
    print("EL AZUL FUE EL MAS VOTADO")