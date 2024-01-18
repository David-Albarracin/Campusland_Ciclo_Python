"""
Hacer un algoritmo que muestre la Serie Fibonacci. 0,1,1,2,3,5,8,13,21,34 

Se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, 
se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores, 
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

a = 0
b = 1
c = 0

#Se usa en el caso que se requiera mostar los numeros en forma de lista
showLista = []

for x in range(10):
    showLista.append(c)
    print(f"{c}")
    a = b
    b = c
    c = a + b