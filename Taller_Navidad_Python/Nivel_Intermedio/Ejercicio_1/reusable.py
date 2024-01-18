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

