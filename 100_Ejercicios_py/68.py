"""
Algoritmo que calcule el salario a pagar de un trabajador.

Debe ingresar por teclado: el sueldo base, el número de hijos y el número de días 
no laborables que asistió el trabajador.

Genere un programa que permita calcular el sueldo final de un empleado, 
si se sabe que el sueldo aumenta en $100 por cada hijo y en $25 por cada día no laborable 
que el trabajador asistió.

"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

SueldoBase = 0
num_hijos = 0
dias_no_laborables = 0
sueldo_final = 0


SueldoBase = reusable.inputFloat("Ingrese Sueldo Base")
num_hijos = reusable.inputFloat("Ingrese Número de Hijos")
dias_no_laborables = reusable.inputFloat("Ingrese Días no Laborables Trabajados")

sueldo_final = SueldoBase + (num_hijos * 100) +(dias_no_laborables * 25)

print(f"SUELDO FINAL : ${sueldo_final}")