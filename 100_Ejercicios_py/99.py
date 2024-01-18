"""
Calcular el monto a pagar por la compra de teclados, el precio varia según su cantidad

Hacer un programa dónde en una tienda que se venden teclados, 
si se compran más de 8 el costo por cada una es de 10 soles; 
entre 4 y 8 es de 11 soles cada una, si la compra es menor de 4 el costo es de 15 soles cada una.

Escriba el algoritmo para saber cuánto pagará el cliente según el número de teclados que ha comprado. 
Mostrar el número de teclados y el total a pagar
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


cantidad = reusable.inputNumber("INGRESE CANTIDAD A COMPRAR")

if (cantidad >= 1 and cantidad <= 3):
    costo = float(15)
elif (cantidad >= 4 and cantidad <= 8):
    costo = float(11)
else:
    costo = float(10)

print(f"Costo por teclado : ${costo}")
print(f"Total a Pagar : ${costo * cantidad}")