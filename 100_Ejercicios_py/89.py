"""
Hacer un algoritmo que muestre el nombre del mes, según el número ingresado del 1 al 12.

Crear un programa que permita ingresar un número del 1 al 12 y 
mostrar el mes correspondiente en nombre: 
Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Setiembre, Octubre, Noviembre o Diciembre.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

mes = reusable.inputNumber("MES [1-12]")

if (mes == 1):
    print(f"Mes de Enero")
elif (mes == 2):
    print(f"Mes de Febrero")
elif (mes == 3):
    print(f"Mes de Marzo")
elif (mes == 4):
    print(f"Mes de Abril")
elif (mes == 5):
    print(f"Mes de Mayo")
elif (mes == 6):
    print(f"Mes de Junio")
elif (mes == 7):
    print(f"Mes de Julio")
elif (mes == 8):
    print(f"Mes de Agosto")
elif (mes == 9):
    print(f"Mes de Septiembre")
elif (mes == 10):
    print(f"Mes de Octubre")
elif (mes == 11):
    print(f"Mes de Noviembre")
elif (mes == 12):
    print(f"Mes de Diciembre")
else:
    print(f"Error Mes Incorrecto")