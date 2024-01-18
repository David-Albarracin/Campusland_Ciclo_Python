"""
Hacer un algoritmo que muestre el nombre y el promedio del alumno con mejor nota
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

bestAlumno = {
    "nombre": "",
    "promedio": 0
}

for x in range(5):
    nombre = input("Ingresa el nombre del alumno :> ")
    promedio = reusable.inputNumber(f"Ingresa el Promedio de {nombre}")
    if (bestAlumno["promedio"] < promedio):
        bestAlumno["nombre"] = nombre
        bestAlumno["promedio"] = promedio


print(f"El Alumno con mayor nota es {bestAlumno['nombre']}")
print(f"El Promedio es {bestAlumno['promedio']}")