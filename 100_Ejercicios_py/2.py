
"""
Hacer un algoritmo que muestre la cantidad de número pares e impares ingresados
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

#Variables para almacenar los numeros pares e impares
pares = []
impares = []

#Creamos un ciclo de 12 pasos donde vamos en pasos de 1 en uno e iremos pidiendo un numero
for x in range(12):
        numero = reusable.inputNumber(f"Numero {(x + 1)}")

        #Clasificamos el numero si es par o impar
        if (numero % 2) == 0:
            pares.append(numero)
        else:
            impares.append(numero)

#Len es una fuincion que se usa para comprobar retornar la catidad de items en un array
print(f"CANTIDAD DE PARES = {len(pares)}")
print(f"CANTIDAD DE IMPARES = {len(impares)}")

reusable.pause()