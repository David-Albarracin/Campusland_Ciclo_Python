"""
Hacer un algoritmo que muestre una gráfica de asteriscos [ * ] 
*******
******
*****
****
***
****
*****
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

xn = 7

for x in range(7):
    serie = ""
    if(x >= 5):
        xn += 2
    for c in range(xn - x):
        serie += "*" 

    print(serie)