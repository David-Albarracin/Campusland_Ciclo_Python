import os
os.system('cls')

mensaje = "hola pepE,"

vocales = 0
consonantes = 0
for caracter in mensaje:
    if (caracter in "aeiou"):
        vocales = vocales + 1
    elif (caracter.isalpha()):
        consonantes = consonantes + 1
    else:
        pass

print("Vocales: ",vocales, "Consonantes: ", consonantes)
