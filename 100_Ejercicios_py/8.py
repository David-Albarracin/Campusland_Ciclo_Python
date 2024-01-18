
"""
Hacer un algoritmo que muestre la serie gráfica de números 123456789 en forma decreciente
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

#Creamos una lista del 1 a el 9
lista = list(range(1, 10))

for x in range(9):
    print(lista)
    ele = lista.pop() #El metodo pop requiere una variable para almacenar el elemento retirado