"""
Algoritmo que muestra el área, base y altura de un triángulo.

Hacer un programa que muestre un menú de opciones de :

A. El valor del área de un triángulo, dada la base y la altura.
B. El valor de la base de un triángulo, dada la altura y el área.
C. El valor de la altura de un triángulo, dada la base y el área.
Dependiendo de la opción A, B ó C, se ejecutara el menú correspondiente.

"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

print(f""" 
MENÚ DE OPCIONES DE UN TRIÁNGULO "

    1. Área de un triángulo, dada la base y la altura"
    2. Base de un triángulo, dada la altura y el área"
    3. Altura de un triángulo, dada la base y el área
"""
)

opcionMenu = reusable.inputNumber("Selecciona una opción")


if (opcionMenu == 1):
    base = reusable.inputFloat("BASE")
    altura = reusable.inputFloat("ALTURA")
    area = (base * altura) / 2
    print(f"EL ÁREA ES : {area}")

elif (opcionMenu == 2):
    altura = reusable.inputFloat("ALTURA")
    area = reusable.inputFloat("ÁREA")
    base = (area * 2) / altura
    print(f"LA BASE ES : {base}")

elif (opcionMenu == 3):
    base = reusable.inputFloat("BASE")
    area = reusable.inputFloat("ÁREA")
    altura = (area * 2) / base
    print(f"LA ALTURA ES : {altura}")

else:
    print(f"Error... Opción Incorrecta")