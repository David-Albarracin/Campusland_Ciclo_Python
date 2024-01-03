import json

data = {
    "id": "001",
    "nombre": "pepe"
}

with open("./Archivos/db.json", "w") as db:
    json.dump({data["id"]:data}, db, indent=2)



