"""
Hacer un algoritmo que muestre el IGV 18% según el monto de compra 

Hacer un programa que permita calcular el IGV 18% de un monto de venta realizado.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


dinero = reusable.inputFloat(f"INGRESE MONTO DE DINERO")

igv = dinero * 0.18

print(f"EL IGV 18% ES : S/. {dinero}")