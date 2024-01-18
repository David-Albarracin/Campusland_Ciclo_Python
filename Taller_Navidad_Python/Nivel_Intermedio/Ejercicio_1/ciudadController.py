import random
import os
import reusable

ciudades = []

ciudadTemplate = {
    "uid": "0",
    "nombre": "1",
    "sismos": "2",
    "riesgo": "3"
}

def newCity():
    if(len(ciudades) < 5):
        opcion = "S"
        while(opcion == "S"):
            os.system("cls")
            uid = random.randint(100, 999)
            nombre = input("Ingresa el Nombre de La Ciudad :> ").lower()
            ciudades.append([uid,nombre,[],0.0])
            print("Ciudad Creada Correctamente")
            opcion = input("Desea Ingresar Otra Ciudad? Si(s) / No(n) :> ").upper()
    else:
        print("Maximo de Ciudades 5")
        os.system("pause")


def newSismo(ciudad: list):
    sismo = reusable.inputFloat(f"Ingresa La Magnitud del sismo para la ciudad {ciudad[1]}")
    sismos:list = ciudad[2]
    sismos.append(sismo)
    cantidadSismos = len(sismos)
    riesgo = 0
    for i in sismos:
        riesgo += i
    ciudad[3] = riesgo / cantidadSismos
    checkCitys(cantidadSismos)


def checkCitys(cantidadSismos):
    for ciudad in ciudades:
        sismos = len(ciudad[2])
        if (sismos < cantidadSismos):
            print("La Catidad De Sismos entre Ciudades No Concide Porfavor")
            newSismo(ciudad)


def searchCity():
    while(True):
        nombre = input("Ingresa el Nombre de la Ciudad :> ")
        for ciudad in ciudades:
            if (nombre in ciudad):
                return ciudad
        print("Ciudad No Encontrada")
        os.system("pause")
        break