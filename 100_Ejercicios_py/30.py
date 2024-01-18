"""
Algoritmo que calcula el total de ventas realizadas por hombres y mujeres de N empleados.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


catidadEmpleados = reusable.inputNumber("Ingresa la Cantidad de Empleados")
empleados = []
mVentas = 0
fVentas = 0

porcMujeres = 0

for i in range(catidadEmpleados):
    nombre = input("Ingresa el Nombre del Empleado :> ")
    genero = input("Ingresa el Genero del Empleado (M/F) :> ").upper()
    ventas = reusable.inputNumber(f"Ingresa el total de Ventas del Empleado {nombre}")
    empleado = {
        "Nombre": nombre,
        "Genero": genero,
        "Ventas": ventas
    }
    if (genero == "M"):
        mVentas += ventas
    else:
        fVentas += ventas
        porcMujeres += 1

    empleados.append(empleado)

print(f"TOTAL DE VENTAS HOMBRES {mVentas}")
print(f"TOTAL DE VENTAS MUJERES {fVentas}")



print(f"PORCENTAJE DE MUJERES {(porcMujeres / len(empleados) * 100)}")

