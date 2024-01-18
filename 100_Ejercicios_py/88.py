"""
Hacer un algoritmo que muestre la estación del año al ingresar un número del 1 al 4

1 = VERANO
2 = OTOÑO
3 = INVIERNO
4 = PRIMAVERA
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

estacion = reusable.inputNumber("NÚMERO [1-4]")

if (estacion == 1):
    print(f"Es Verano")
elif (estacion == 2):
    print(f"Es Otoño")
elif (estacion == 3):
    print(f"Es Invierno")
elif (estacion == 4):
    print(f"Es Primavera")