"""
Sumatoria de 4/2 – 9/1 + 15/1 – 23/2 + 34/8 – 49/64.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable



sumatoria = 0
v = 4
v1 = 5
v2 = 1
x = 2
x1 = 0.5
ope = "-"

numero = reusable.inputNumber("Ingresa un Numero")

for i in range(1, numero + 1):
    if (i != numero):
        print(f"{v}/{x} {ope} ", end = "")
    else:
        print(f"{v}/{x} {ope} ...", end = "")
    if ((i % 2) == 1):
        ope = "+"
        sumatoria = sumatoria + (v / x)
    else:
        ope = "-"
        sumatoria = sumatoria - (v / x)
    v = v + v1
    v1 = v1 + v2
    v2 = v2 + 1
    x = x * x1
    x1 = (x1 + x1)


print(f"SUMATORIA : {sumatoria}")