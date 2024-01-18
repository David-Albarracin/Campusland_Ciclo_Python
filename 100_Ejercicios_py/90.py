"""
Hacer un algoritmo que muestre las cuatro operaciones básicas

Introducir dos números enteros y un operador (+, -, *, /); según el operador seleccionado, realizar y mostrar la operación matemática correspondiente.

"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

num1 = reusable.inputNumber("NÚMERO 1")
num2 = reusable.inputNumber("NÚMERO 2")

print("""
    [1 +]
    [2 -]
    [3 x]
    [4 /]
"""
)
operador = reusable.inputNumber("OPERADOR")

if (operador == 1):
    print(f"SUMA : {(num1 + num2)}")
elif (operador == 2):
    print(f"RESTA : {(num1 - num2)}")
elif (operador == 3):
    print(f"MULTIPLICACIÓN : {(num1 * num2)}")
elif (operador == 4):
    print(f"DIVISIÓN : {(num1 / num2)}")
else:
    print(f"OPERADOR INCORRECTO")