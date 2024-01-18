"""
Algoritmo que muestra si un número es o no capicúa
"""


#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

numero = str(reusable.inputNumber("Ingresa Un Numero Para Verificar si es capicúa"))

if (numero == (numero[::-1])):
    print("SI ES UN NUMERO CAPICUA")
else: 
    print("NO ES UN NUMERO CAPICUA")