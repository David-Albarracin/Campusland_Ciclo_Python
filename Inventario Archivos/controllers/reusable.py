



def checkInput(typeData:"int" or "float",message):
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