"""
Algoritmo que muestra la cantidad de números pares e impares ingresados 
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


pares = ""
impares = ""



for i in range(5):
    numero = reusable.inputNumber(f"Ingresa Un Numero")
    if ((numero % 2) == 0 ):
        pares += f"{numero} "
    else:
        impares += f"{numero} "

print(f"Numeros Pares {pares}")
print(f"Numeros Impares {impares}")