import random
import os
import co2Controller as co2
import reusable

dependencias = []


def newDependencia():
    os.system("cls")
    opcion = True
    while(opcion):
        uid = random.randint(100, 999)
        nombre = input("Ingresa el Nombre de la Dependencia :> ")
        dependencia = {
            "uid": uid,
            "nombre": nombre,
            "dispositivos": 0,
            "transporte": 0,
            "CO2": 0
        }
        dependencias.append(dependencia)
        print(f"Dependencia {nombre} Creada Correctamente")
        opcion = reusable.yesORnot("¿Desea Ingresar otra Dependencia?")


def registrarConsumo():
    while(True):
        os.system("cls")
        dependencia = searchDependencia()
        if(dependencia):
            dependencia = co2.co2Encuesta(dependencia)
            os.system("cls")
            print("Dependencia Actualizada Correctamente")
            opcion = reusable.yesORnot("Desea Ingresar el consumo de otra Dependencia")
            if(not opcion):
                break
    return
        



def searchDependencia():
    while(True):
        nombre = input("Ingresa el Nombre de la Dependencia :> ")
        for dependencia in dependencias:
            if (nombre in dependencia["nombre"]):
                return dependencia
        print("Ciudad No Encontrada")
        os.system("pause")
        break

def moreCo2():
    mDependencia = {
        "nombre": "Ingresa Dependencias",
        "CO2": 0
    }
    for dependencia in dependencias:
        if(dependencia["CO2"] > mDependencia["CO2"]):
            mDependencia = dependencia
    return dependencia