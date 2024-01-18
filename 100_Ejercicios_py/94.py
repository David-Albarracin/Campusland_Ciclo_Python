"""
Hacer un algoritmo que muestre el sueldo a pagar de un empleado según su categoría

Categoría = Bonificación :
A = 10%
B = 20%
C = 30%
D = 50%
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

bonificacion = 0


sueldo = reusable.inputNumber("Sueldo Base")
categoria = reusable.inputNumber("Categoría : 1.A - 2.B - 3.C - 4.D")

if (categoria == 1):
    bonificacion = sueldo * 0.1
elif (categoria == 2):
    bonificacion = sueldo * 0.2
elif (categoria == 3):
    bonificacion = sueldo * 0.3
elif (categoria == 4):
    bonificacion = sueldo * 0.5

print(f"BONIFICACIÓN : ${bonificacion}")
print(f"SUELDO NETO :  ${sueldo + bonificacion}")