"""
Hacer un algoritmo que muestre los días transcurridos desde el inicio del año hasta ahora

ngresar la fecha actual y mostrar el número total de días transcurridos desde el inicio de este año,
considerando que todos los meses tienen 30 días.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

print("Ingresa la fecha Actual\n")

dia = reusable.inputNumber("Ingresa el Dia")
mes = reusable.inputNumber("Ingresa el Mes")
year = reusable.inputNumber("Ingresa el Año")

dias = (((mes - 1) * 30) + dia)

print(f"DIAS TRASCURRIDOS EN EL AÑO {year} es : {dias}")

