"""
Algoritmo que muestra el porcentaje de alumnos aprobados y desaprobados

Ingrese la cantidad de alumnos aprobados y desaprobados de un curso, 
luego mostrar el porcentaje de estudiantes aprobados y el porcentaje de estudiantes desaprobados.

"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


apro = reusable.inputNumber("INGRESE LA CANTIDAD DE ALUMNOS APROBADOS")
desa = reusable.inputNumber("INGRESE LA CANTIDAD DE ALUMNOS DESAPROBADOS")

porA = (apro * 100) / (apro + desa)
porB = (desa * 100) / (apro + desa)

print(f"APROBADOS : {round(porA * 100) / 100}%")
print(f"DESAPROBADOS : {round(porB * 100) / 100}%")