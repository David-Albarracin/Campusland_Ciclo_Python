"""
Algoritmo que muestre el nombre completo de un programa al ingresar su primera letra.

Crea una variable para almacenar la primera letra de los siguientes lenguajes de programación: 
Visual Basic, Pascal, C#, Java, Fortran. Dependiendo de la letra ingresada, 
muestra el lenguaje de programación correspondiente en pantalla. 
Si la letra no pertenece a ningún lenguaje de programación, muestra un mensaje de error.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

letra = input(f"Letra [V - P - C - J - F] : ").upper()

if (letra == "V"):
    print(f"Visual Basic")
elif (letra == "P"):
    print(f"Pascal")
elif (letra == "C"):
    print(f"C#")
elif (letra == "J"):
    print(f"Java")
elif (letra == "F"):
    print(f"Fortran")