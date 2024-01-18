"""
Hacer un algoritmo que dibuje un rombo de asteriscos

Hacer un programa que permita ingresar un número impar y según el número ingresado se 
dibuje la figura geométrica de un rombo, se debe validar para que no acepte números pares.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

altura = 0

while ((altura % 2) != 1):
    altura = reusable.inputNumber("Altura del rombo")

for i in range(1, altura + 1, 2):
    for j in range(1, int((altura - i)/2 + 1)):
        print(f" ", end = "")
    for j in range(1, i + 1):
        print(f"*", end = "")
    print("")

for i in reversed(range(1, altura - 1, 2)):
    for j in range(1, int((altura - i)/2 + 1)):
        print(f" ", end = "")
    for j in range(1, i + 1):
        print(f"*", end = "")
    print("")