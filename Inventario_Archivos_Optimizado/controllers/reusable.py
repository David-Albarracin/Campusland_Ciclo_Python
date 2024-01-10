import os


def showError(message):
    pass

def showSuccess():
    pass


def checkInput(typeData,message):
    while True:
        try:
            if typeData == "int":
                number = int(input(message))
            elif typeData == "float":
                number = float(input(message))
        except ValueError:
            print("Error Al Ingresar el Dato Solo Ingresa Numeros....")
        else:
            return number