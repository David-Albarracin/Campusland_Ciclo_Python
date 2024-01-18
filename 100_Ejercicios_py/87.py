"""
Hacer un algoritmo que muestre un número en romanos

Hacer un programa que ingrese un número del 1 al 10 y muestre el mismo número pero en Romanos.

EJEMPLO :
-----------------
1 = 1
2 = II
3 = III
4 = IV
5 = V
6 = VI
7 = VII
8 = VIII
9 = IX
10 = X
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

num = reusable.inputNumber("INGRESE NÚMERO DEL 1 AL 10")

if (num == 1):
    print(f"En Romanos : I")
elif (num == 2):
    print(f"En Romanos : II")
elif (num == 3):
    print(f"En Romanos : III")
elif (num == 4):
    print(f"En Romanos : IV")
elif (num == 5):
    print(f"En Romanos : V")
elif (num == 6):
    print(f"En Romanos : VI")
elif (num == 7):
    print(f"En Romanos : VII")
elif (num == 8):
    print(f"En Romanos : VIII")
elif (num == 9):
    print(f"En Romanos : IX")
elif (num == 10):
    print(f"En Romanos : X")
else:
    print(f"Error...sólo de 1 a 10")