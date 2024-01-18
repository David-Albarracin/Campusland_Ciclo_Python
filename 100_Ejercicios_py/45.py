"""
Hacer un algoritmo que calcule las medidas de una pared según el alto y largo ingresado.

Un constructor sabe que necesita 0,05 metros cúbicos de arena por metro cuadrado de revoque a realizar. 
Hacer un algoritmo que calcule las medidas de una pared en largo y alto expresada 
en metros y obtenga la cantidad de arena necesaria para el revoque total.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

alto = reusable.inputNumber("Ingresa el ALTO de la Pared en MTS")
largo = reusable.inputNumber("Ingresa el LARGO de la Pared en MTS")

arena = ((alto * largo) * 0.25)

print(f"Área Necesaria : {arena} mt3.")