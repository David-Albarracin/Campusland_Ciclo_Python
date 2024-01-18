"""
Algoritmo que ingrese un refrán y muestre el número de letras C, S, D, L, R y M que hay
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


refran = input("Ingresa un Refran :>").upper()

c=0
s=0
d=0
l=0
r=0
m=0

consonante = 0

for i in refran:
    if (i == "C"):
        c += 1
    elif(i == "S"):
        s += 1
    elif(i == "D"):
        d += 1
    elif(i == "L"):
        l += 1
    elif(i == "R"):
        r += 1
    elif(i == "M"):
        m += 1
    elif((i == "A") or (i == "E") or (i == "I") or (i == "O") or (i == "U")):
        consonante += 1


print(f"CANTIDAD DE C {c}")
print(f"CANTIDAD DE S {s}")
print(f"CANTIDAD DE D {d}")
print(f"CANTIDAD DE L {l}")
print(f"CANTIDAD DE R {r}")
print(f"CANTIDAD DE M {m}")

print(f"CANTIDAD DE CONSONANTES {consonante}")