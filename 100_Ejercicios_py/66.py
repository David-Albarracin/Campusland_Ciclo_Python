"""
Hacer un algoritmo que dibuje un triangulo con un carácter ingresado

Hacer un programa que permita ingresar el tamaño que tendrá un triángulo, 
el cual debe ser dibujado según un carácter ingresado. Por ejemplo : 
Puede ser un triángulo de asteriscos u otro carácter ingresado.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

altura = reusable.inputFloat("Altura del Triángulo")
caracter = reusable.inputFloat("Ingrese un Caracter")

for i in range(1, altura + 1):
    for j in range(1, (altura - i) + 1):
        print(f" ", end = "")
    for j in range(1, (i * 2)):
        print(caracter, end = "")
    print(f"")