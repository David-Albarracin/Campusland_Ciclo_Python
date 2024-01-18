"""
Algoritmo que muestre el descuento a pagar según el monto de compra en un supermercado.

En la tienda de comestibles, los clientes deben pulsar un botón al realizar sus compras. 
Dependiendo del color de la luz que se encienda, recibirán un porcentaje de 
descuento en función del valor total de su compra, según lo indicado en la tabla de precios.

Color = Descuento (%)
————————
Blanco = 100%
Verde = 50%
Negro = 40%
Celeste = 5%
Rojo = 0%

Calcular el descuento y el pago final (valor compra menos descuento) que realizará un cliente.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable
import random


desct = 0
compra = 0


compra = reusable.inputNumber("VALOR DE COMPRA")
color = random.randint(1, 5)


if (color == 1):
    print(f"COLOR : BLANCO")
    desct = 1
elif (color == 2):
    print(f"COLOR : VERDE")
    desct = 0.5
elif (color == 3):
    print(f"COLOR : NEGRO")
    desct = 0.4
elif (color == 4):
    print(f"COLOR : CELESTE")
    desct = 0.05
elif (color == 5):
    print(f"COLOR : ROJO")
    desct = 0

print(f"DESCUENTO : ${desct}")
print(f"IMPORTE DESCT. : ${compra * desct}")
print(f"PAGO FINAL : ${compra - (compra * desct)}")