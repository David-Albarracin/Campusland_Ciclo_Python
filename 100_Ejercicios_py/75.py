"""
Hacer un algoritmo que calcule el descuento a pagar según el monto de compra

Hacer un programa que según el monto de compra calcular su descuento, 
considerando que por encima de $350, 
el descuento es del 35% y por debajo de $350 el descuento es de 10%.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

monto = reusable.inputNumber("MONTO DE LA COMPRA")

if (monto >= 350):
    desct = monto * 0.35
    print(f"DESCUENTO ES DE 35% : ${desct}")
else:
    desct = monto * 0.10
    print(f"DESCUENTO ES DE 10% : ${desct}")

print(f"MONTO A PAGAR : ${monto - desct}")