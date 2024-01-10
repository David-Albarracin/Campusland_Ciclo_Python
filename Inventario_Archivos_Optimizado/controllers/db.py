import json
import os

PATH = "./Inventario Archivos/data/"
URL = ''

def saveData(**data):
    with open(f"{PATH}{URL}", "w") as archivo:
        json.dump(data, archivo, indent=4)

def loadData(**data):
    file = os.path.isfile(f"{PATH}{URL}")
    if(not file):
        saveData(**data)
        return data
    else:
        with open(f"{PATH}{URL}", "r") as archivo:
            return json.load(archivo)