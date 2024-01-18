"""
Este documento py se realiza con el fin de reutulizar funciones 
que se repetiran al momento de realizar los 100 ejercicios 

"""

import os

#Funcion para parar el programa en ejecucion
def pause():
    os.system("pause")

def cls():
    os.system("cls")

#Funcion para que el usuario ingrese solo numeros
def inputNumber(message) -> int:
    #Variable que almacena el estado del dato True(Si es Numero) Falso(si no)
    validNumber = False

    #Ciclo para continuar con el programa solo si el usuario ingresa un dato valido 
    while(not validNumber):

        #verificando la integridad de la información ingresada.
        try:
            #Variable que almacena un numero del usuario
            numero = int(input(f"{message} :> "))
        except:
            cls()
            print("Error Ingresa un Dato Valido")
        else:
            validNumber = True
            return numero
        
#Funcion para que el usuario ingrese solo numeros flotantes
def inputFloat(message) -> int:
    #Variable que almacena el estado del dato True(Si es Numero) Falso(si no)
    validNumber = False

    #Ciclo para continuar con el programa solo si el usuario ingresa un dato valido 
    while(not validNumber):

        #verificando la integridad de la información ingresada.
        try:
            #Variable que almacena un numero del usuario
            numero = float(input(f"{message} :> "))
        except:
            cls()
            print("Error Ingresa un Dato Valido")
        else:
            validNumber = True
            return numero