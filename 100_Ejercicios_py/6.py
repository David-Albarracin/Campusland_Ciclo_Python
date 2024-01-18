"""
Algoritmo que muestre la siguiente progresión aritmética : 1,5,7,10,13,15,19,20,25,25
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

var = 1
a = 1
b = 5

#Se usa en el caso que se requiera mostar los numeros en forma de lista
showLista = []

for x in range(1,10):
    showLista.append(a)
    showLista.append((x * 5))
    print(f"{a}")
    print(f"{x * 5}")
    a += 6

print(showLista)