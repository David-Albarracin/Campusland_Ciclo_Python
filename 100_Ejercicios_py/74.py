"""
Hacer un algoritmo que muestre si un número ingresado es capicúa

Hacer un programa dónde se ingrese un número entero de 3 cifras y muestre si es o no, 
un número capicúa. Se enciende como un número capicúa cuando al intercambiar los valores de sus 
extremos nos da el mismo valor. Ejemplo : 242, 131, 565, etc.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

num = 0
while (num <= 100) and (num <= 999):
    num = reusable.inputNumber("INGRESE NÚMERO DE 3 CIFRAS")

c1 = (num - (num % 100)) / 100
r1 = num % 100
c2 = (r1 - (r1 % 10)) / 10
r2 = r1 % 10

if (num == ((r2 * 100) + (c2 * 10) + c1)):
    print(f"NÚMERO CAPICÚA")
else:
    print(f"NO ES CAPICÚA")