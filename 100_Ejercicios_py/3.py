"""
Hacer un algoritmo que calcule el monto a pagar por 10 compras realizadas
Aplicarle un descuento de 7% si el total de las compras es superior a 50
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

#Variable para guardar el total a pagar
totalPagar = 0


for x in range(10):
    cantidad = reusable.inputNumber(f"COMPRA NUMERO {x + 1}")
    totalPagar += cantidad

#Variable para guardar el valor del descuento del 7%
descuento = 0
if (totalPagar > 50):
    descuento = totalPagar * 0.07
print(f"Consumo total: ${totalPagar}")
print(f"Descuento: -${round(descuento, 1)}")
print(f"Total a Pagar: ${totalPagar - descuento}")