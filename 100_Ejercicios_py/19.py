"""
Hacer un algoritmo que muestre la tabla de multiplicar de cualquier número ingresado.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

numero = reusable.inputNumber("Ingresa un Numero Para Saber Su Tabla de Multiplicar")

#Creamos un ciclo de 12 pasos donde vamos en pasos de 1 en uno y lo multiplicamos por el numero ingresado
for x in range(12):
        print(f"{numero} x {x} = {numero * x}")
    
reusable.pause()