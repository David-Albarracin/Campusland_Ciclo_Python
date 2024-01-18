import os


def inputFloat(message:str):
    while(True):
        try:
            numero = float(input(f"{message} :> "))
        except: 
            print("Ingresa un Dato Valido")
        else:
            break
        
    return numero

def inputNumber(message:str):
    while(True):
        try:
            numero = int(input(f"{message} :> "))
        except: 
            print("Ingresa un Dato Valido")
        else:
            break
        
    return numero

def yesORnot(message):
    while(True):
        try:
            opcion = input(f"{message} Si(s) o No(n) :> ").upper()
        except: 
            print("Ingresa un Dato Valido (S) o (N)")
        else:
            if(opcion == "S"):
                return True
            elif(opcion == "N"):
                return False
            else:
                print("Ingresa un Dato Valido (S) o (N)")
        