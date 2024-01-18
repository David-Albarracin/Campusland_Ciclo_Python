"""
Hacer un algoritmo que muestre el total a pagar por la compra de teclados

Crea una aplicación donde una tienda vende teclados. 
Si se compran más de 8 teclados, el costo por unidad es de 10 soles, 
si se compran entre 4 y 8 el costo por unidad es de 11 soles, y 
si se compran menos de 4 el costo es de 15 soles por unidad. 
Diseña un algoritmo para calcular el costo total a pagar según la cantidad de teclados comprados. 
Muestra el número de teclados y el costo total en pantalla.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

cantidad = reusable.inputNumber("Cantidad a comprar")

if (cantidad >= 1 and cantidad <= 3):
    costo = 15
elif (cantidad >= 4 and cantidad <= 8):
    costo = 11
else:
    costo = 10

print(f"Costo por teclado : ${costo}")
print(f"Total a Pagar : ${costo * cantidad}")