"""
Hacer algoritmo que calcule el salario a pagar de un empleado, con un descuento del 20%.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


saldo = reusable.inputNumber("INGRESA EL SALARIO A PAGAR")

descuento = saldo * 0.2

print(f"SUELDO : ${saldo}")
print(f"DESCUENTO : ${descuento}")
print(f"Total a Pagar : ${saldo - descuento}")