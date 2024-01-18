"""
Hacer un algoritmo que muestre si ¿Chile fue al Mundial de Rusia 2018? 

Hacer un programa que nos permita responder con Verdadero o Falso si Chile 
llego a ir al Mundial Rusia 2018, usar tipo de dato Lógico.

NOTA: Desarrollamos este código para aprovechar la tendencia del momento, 
no era, ni es nuestra intención incomodar a nuestros hermanos chilenos.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

dato = bool(input("Chile Jugo en el Mundial de Rusia 2018 si(S) / no(Enter)"))

if (dato):
    print(f"Está equivocado, no fue al Mundial")
else:
    print(f"Está en lo correcto, no fue al Mundial")