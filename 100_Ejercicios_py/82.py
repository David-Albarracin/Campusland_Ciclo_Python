"""
Hacer un algoritmo que calcule el IGV 18% del monto a pagar, si el monto es mayor a $500.

Ejercicio que se desarrollara en este caso es: 
ingresar un número si es mayor a 500 calcular el 18%, 
por lo que deberás ingresar un número si es mayor de 500 se debe 
calcular y mostrar en pantalla el 18% de este.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

monto = reusable.inputNumber("INGRESE MONTO")

if (monto > 500):
    print(f"EL 18% ES : ${(monto * 0.18)}")