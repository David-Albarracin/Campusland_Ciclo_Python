import json
import os

PATH = "./Inventario Archivos"
URL = ''

def NewFile(data:dict):
    with open(f"{PATH}{URL}", "w") as wf:
        json.dump(data, wf, indent=4)

def checkFile():
    file = os.path.isfile(f"{PATH}{URL}")
    if(not file):
        NewFile({})