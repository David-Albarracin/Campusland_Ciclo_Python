import json
import os


URL = "data/db.json"

data = {
    "blockbuster":{
        "peliculas":{}
    }
}

peliculaInterface = {
    "P01":{
        "id": "P01",
        "nombre": "Rambo",
        "duracion": "80",
        "sinopsis": "10 de enero a las dos de la mañana era un dia",
        "generos": {
            "G01": {
                "id": "G01",
                "nombre": "accion"
            }
        },
        "actores": {
            "A01":{
                "id": "A01",
                "nombre": "silvester stallone",
                "rol": "protagonista"#| antagonista | reparto
            }
        },
        "formato": {
            "F01": {
                "id": "F01",
                "nombre": "DVD",
                "NroCopias": 2,
                "valorPrestamo": 5000
            },
            "F02": {
                "id": "F01",
                "nombre": "BlueRay",
                "NroCopias": 4,
                "valorPrestamo": 6000
            }
        }
    }
}

def saveData(**data):
    with open(URL, "w") as archivo:
        json.dump(data, archivo, indent=4)


def loadData(**data):
    if os.path.isfile(URL):
        with open(URL, "r") as archivo:
            return json.load(archivo)
    else:
        saveData(**data)
        return data