"""
Hacer un algoritmo que muestre la serie : 1 + 2/3 + 3/5 + 4/7 
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable
d = 3
suma = 1

n = reusable.inputNumber("VALOR DE N")

if (n > 1):
    print(f"{suma} + ", end = "")
    for i in range(2, n + 1):
        if (i == n):
            print(f"{i}/{d}", end = "")
        else:
            print(f"{i}/{d} + ", end = "")
        suma += (i/d)
        d = d + 2
        

print(f"\nLa suma es : {suma}")