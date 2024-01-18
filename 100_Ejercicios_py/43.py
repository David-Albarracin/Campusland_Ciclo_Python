"""
Algoritmo que muestre cuantas entradas al cine se pueden comprar con un monto ingresado.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


monto = reusable.inputNumber("CUANTO DINERO TIENES : ")

monto = (monto / 15)

print(f"Puedes Comprar {monto} Entradas")