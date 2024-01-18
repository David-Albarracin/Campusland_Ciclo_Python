"""
Hacer un algoritmo que calcule el IGV si el monto de compra es mayor a $100 USA

Hacer un programa que solicite el precio y la cantidad de compra; 
si el monto es mayor a S/.100 calcular el IGV. Mostrar el total a pagar y IGV si lo hubiera.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

IGV = 0
monto = 0

precio = reusable.inputNumber("INGRESE PRECIO")
cant = reusable.inputNumber("INGRESE CANTIDAD")

monto = (precio * cant)

if (monto > 100):
    IGV = monto * 0.18

print(f"TOTAL : ${monto}")
print(f"IGV 18% : ${IGV}")
print(f"TOTAL A PAGAR : ${(monto + IGV)}")