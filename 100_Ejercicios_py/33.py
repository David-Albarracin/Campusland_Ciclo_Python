"""
Ingresar una frase y mostrar la cantidad de vocales que contiene.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


palabra = input("Ingresa una Frace para Saber Cuantas Vocales Tiene :> ").upper()

vocales = 0


for i in palabra:
    if((i == "A") or (i == "E") or (i == "I") or (i == "O") or (i == "U")):
        vocales += 1

print(f"TIENE {vocales} VOCALES")