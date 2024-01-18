"""
Hacer un algoritmo que al ingresar las horas, minutos y segundos, calcule el costo total

Escriba un programa dónde se ingrese el tiempo necesario para un proceso en horas, minutos y segundos.
Calcule el costo total del proceso sabiendo que el costo por segundo es $0,25.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

horas = reusable.inputNumber("HORAS")
minutos = reusable.inputNumber("HORAS")
segundos = reusable.inputNumber("HORAS")

costo = ((horas * 3600) + (minutos * 60) + segundos) * 0.25


print(f"COSTO TOTAL : {costo}")