"""
Hacer un algoritmo que muestre el producto de varios números ingresados
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable

#Variable para Guardar el numero ingresado por el usuario
numero = reusable.inputNumber("Valor de N")
#Variable para producto de tipo acumulativo
prod = 1

#guardamos los numero para mostrarlos en una sola linea 
listNumber = ""

for x in range(1, (numero + 1)):
    listNumber += f"{x} "
    prod = (prod * x)

print(listNumber)
print(f"El producto de {numero} es = {prod}")