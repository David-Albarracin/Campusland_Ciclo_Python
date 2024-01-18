"""
Hacer un algoritmo que muestre el monto a pagar según el tipo de seguro elegido [X - Y - Z]

Una compañía aseguradora ofrece a sus clientes tres opciones de seguro, [X | Y | Z]. Tipo de seguro | Costo mensual ($):
X | $45
Y | $30
Z | $15
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

print("""
TIPOS DE SEGURO"
    1. X"
    2. Y"
    3. Z
"""
)

seguro = reusable.inputNumber("OPCIÓN")

if (seguro == 1):
    print(f"Pago Mensual : $45")
elif (seguro == 2):
    print(f"Pago Mensual : $30")
elif (seguro == 3):
    print(f"Pago Mensual : $15")
else:
    print(f"Error en el tipo de seguro.")