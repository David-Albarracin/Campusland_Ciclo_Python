"""
Hacer un algoritmo que muestre todos los números que estén en el rango de A y B
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

numeroUno = reusable.inputNumber("Numero A")
numeroDos = reusable.inputNumber("Numero B")

numberMayor = 0

if(numeroUno < numeroDos):
    for i in range(numeroUno, numeroDos):
        print(i)
else:
    for i in range(numeroDos, numeroUno):
       print(i)
