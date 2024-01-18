import json
import os


PATH = "./Nivel_Experto/db/"
URL = ""



def newFile(**kwargs):
    with open(f"{PATH}{URL}", "w") as archivo:
        json.dump(kwargs, archivo, indent=4)


def loadData():
    with open(f"{PATH}{URL}", "r") as archivo:
        return json.load(archivo)
    


def checkFile(**kwargs):
    if(os.path.isfile(f"{PATH}{URL}")):
        kwargs.update(loadData())
    else:
        newFile(**kwargs)

    return kwargs

def updateDataBases():
    import services.campers as campers
    import services.campusland as campus
    with open(f"{PATH}{campus.URL}", "w") as archivo:
        json.dump(campus.campuslandDB, archivo, indent=4)
        archivo.close

    with open(f"{PATH}{campers.URL}", "w") as archivo:
        json.dump(campers.campers, archivo, indent=4)
        archivo.close

"""
def updateFile(**kwargs):
    with open(f"{PATH}{URL}","r+") as archivo:
        data = json.load(archivo)
        data.update(kwargs)
        archivo.seek(0)
        json.dump(data,archivo,indent=4)
"""