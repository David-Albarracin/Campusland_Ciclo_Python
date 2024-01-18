"""
Hacer un programa que ingrese un número del 1 al 7 y muestra que día de la semana es

Realizar un algoritmo que al ingresar un número del 1 al 7, 
muestre el día de la semana correspondiente siendo el 1 para el Lunes, 
de lo contrario mostrar un mensaje de ERROR.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

dia = reusable.inputNumber("INGRESE DÍA [1-7]")

if (dia == 1):
    print(f"LUNES")
elif (dia == 2):
    print(f"MARTES")
elif (dia == 3):
    print(f"MIERCOLES")
elif (dia == 4):
    print(f"JUEVES")
elif (dia == 5):
    print(f"VIERNES")
elif (dia == 6):
    print(f"SÁBADO")
elif (dia == 7):
    print(f"DOMINGO")
else:
    print(f"Día Inválido")