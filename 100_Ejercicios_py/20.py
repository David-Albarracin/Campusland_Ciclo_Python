"""
Hacer un algoritmo que busque un número que se ha generado de forma aleatoria
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable
import random

vidas = 4
randomNumber = random.randint(1, 10)
message = f"FELICIDADES GANASTE EL NUMERO ADIVINAR ERA {randomNumber}"

print("Se genero un Numero Aleatorio entre 1-10 Tienes 3 Vidas Para adivinar")

while(vidas):
    numero = reusable.inputNumber("Ingresa un Numero del 1-10")
    reusable.cls()
    if (numero == randomNumber):
        vidas = 0
    else:
        vidas -= 1
        print(f"Te quedan {vidas}")
        if (numero < randomNumber):
            print("El Numero es Mayor")
        else:
            print("El Numero es Menor")
        if (vidas == 0):
            message = f"PERDIESTE EL NUMERO ADIVINAR ERA {randomNumber}"


print(message)