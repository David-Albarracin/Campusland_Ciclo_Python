import os


def checkInput(typeData, message):
    while True:
        try:
            data = input(f"{message} :> ")
            if typeData == "int":
                data = int(data)
        except ValueError:
            printInfo("Error Ingresa Datos Validos")
        else:
            if (typeData == "str") and (len(data) < 1):
                printInfo("Error Ingresa Datos Validos")
            else:
                return data


def breakWhile(header, message):
    os.system("cls")
    while True:
        print(f"+ {header} +")
        opcion = (checkInput("str", f"{message} Si(s) o No(n)")).upper()
        if opcion == "S":
            os.system("cls")
            return False
        elif opcion == "N":
            os.system("cls")
            return True
        else:
            os.system("cls")
            printInfo("Ingresa (S) para Si o (N) para No.....")
            os.system("pause")

def printInfo(message):
    os.system("cls")
    print(message)
    os.system("pause")



def filterFor(key, forFilter, **data):
    d = [element for element in data if element[key] == forFilter]
    return d


def uuid(category:str, data:list):
    firstCaracter = category[0].upper()
    lenData = len(data)
    if (lenData < 9) and (lenData > 0):
        return f"{firstCaracter}0{lenData + 1}"
    elif (lenData == 0):
        return f"{firstCaracter}01"
    else:
        return f"{firstCaracter}{lenData}"