"""
Hacer un algoritmo que calcule la bonificación a pagar

Hacer un programa que asigna una determinada 
bonificación a sus empleados según el monto total de sus venta, 
si el monto total de las ventas es mayor a $2000 asignar una bonificación del 10%, 
caso contrario dar una bonificación del 5%.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

venta = reusable.inputFloat("INGRESE MONTO DE VENTA ")

if (venta > 2000):
    print(f"BONIFICACIÓN 10% : $.{venta * 0.10}")
else:
    print(f"BONIFICACIÓN 50% : $.{venta * 0.50}")