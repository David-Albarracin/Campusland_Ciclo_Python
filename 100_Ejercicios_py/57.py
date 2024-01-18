"""
ALGORITMO QUE MUESTRA LA CANTIDAD DE AÑOS, MESES Y DÍAS QUE HAY EN UNA FECHA INGRESADA.

Ingresar un número de días y mostrar la cantidad de años, 
meses y días que hay en el valor ingresado; considerar que todos los meses tienen 30 días.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable
import math

dias = reusable.inputNumber("Ingrese los Dias")

year = math.trunc(dias / 365)
mes = math.trunc((dias - (year * 365)) / 30)
dia = math.trunc(dias - ((year * 365) + (mes * 30)))

print(f"Año : {year}")
print(f"Mes : {mes}")
print(f"Día : {dia}")