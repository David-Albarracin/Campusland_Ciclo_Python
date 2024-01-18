"""
Hacer un algoritmo que muestre el nivel académico de un alumno según la nota ingresada.

Introduce 3 notas y calcula el promedio de un estudiante. Según el promedio obtenido, obtén el nivel académico del estudiante :
* De 00 a 10 = Malo.
* De 11 a 13 = Regular.
* De 14 a 16 = Bueno.
* De 17 a 20 = Muy bueno
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

N1 = reusable.inputNumber("Ingrese Nota 1")
N2 = reusable.inputNumber("Ingrese Nota 2")
N3 = reusable.inputNumber("Ingrese Nota 3")

prom = round((N1 + N2 + N3)/3)

if (prom >= 0 and prom <= 10):
    print(f"NIVEL MALO")
elif (prom >= 11 and prom <= 13):
    print(f"NIVEL REGULAR")
elif (prom >= 14 and prom <= 16):
    print(f"NIVEL BUENO")
elif (prom >= 17 and prom <= 20):
    print(f"NIVEL MUY BUENO")