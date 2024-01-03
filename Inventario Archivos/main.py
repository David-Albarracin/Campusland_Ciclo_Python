if __name__ == "__main__":
    pass



import json

data = {
    "id": "001",
    "nombre": "pepe"
}

data.pop()

with open("./Archivos/db.json", "w") as db:
    json.dump({data["id"]:data}, db, indent=2)



