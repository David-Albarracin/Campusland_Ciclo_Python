"""
Algoritmo que muestra si un número ingresado es primo
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


numero = reusable.inputNumber(f"Ingresa Un Numero PRIMO")
isPrime = "ES PRIMO"

for i in range(2,numero):
    if (numero%i) == 0:
      isPrime = "NO ES PRIMO"
    

print(isPrime)