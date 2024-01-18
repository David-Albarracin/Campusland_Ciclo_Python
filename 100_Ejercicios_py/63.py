"""
Hacer un algoritmo que calcule el IVA del monto total a pagar

Hacer un algoritmo que muestre el IVA a pagar por la venta de una casa. 
Ingresar el valor de venta de la casa y el porcentaje de IVA a calcular.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


costo = reusable.inputNumber("Costo de la Casa")
iva = reusable.inputNumber("Valor del IVA")

TotPagar = costo + (costo * (iva / 100))

print(f"IVA DE {iva}% : ${(costo * (iva / 100))}")
print(f"TOTAL A PAGAR : ${TotPagar}")