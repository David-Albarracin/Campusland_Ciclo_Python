"""
Hacer un algoritmo que muestra el total a pagar por un préstamo del banco

Hacer un algoritmo dónde una persona recibe un préstamo de $1000 de un banco
desea saber cuánto pagará de interés, 
si el banco le cobra una tasa del 2% mensual. 
Ingresar el número de meses por teclado.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


meses = reusable.inputNumber("Ingresa el Numero de Meses : ")

interes = (1000 * 0.02)

print(f"Total de Interes a Pagar por {meses} Meses es: {interes}")