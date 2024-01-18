"""
Dibuja un triángulo equilátero de números en secuencia.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

num = 0
val = 1
contador = 1


while (num < 3):
    num = reusable.inputNumber("Ingresa un Numero")


for x in range(1, num + 1):
    espa = ""
    for z in range(1, num - x + 1):
        espa = espa + " "
    print(espa, end = "")
    contador = 1
    for f in range(1, val + 1):
        print(contador, end = "")
        if (contador == 9):
            contador = 0
        else:
            contador = contador + 1
    val = val + 2
    print(f"")