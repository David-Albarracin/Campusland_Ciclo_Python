"""
Hacer un programa que simule un login o clave de acceso

Elaborar un programa que simule una clave de acceso. 
Si el usuario es : ADMIN y la clave : 123456 mostrar el mensaje 
ACCESO PERMITIDO caso contrario mostrar ACCESO DENEGADO.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

usuario = input("INGRESE USUARIO")
clave = reusable.inputNumber("INGRESE CODIGO ")

if (usuario == "ADMIN" and clave == 123456):
    print(f"ACCESO PERMITIDO")
else:
    print(f"ACCESO DENEGADO")