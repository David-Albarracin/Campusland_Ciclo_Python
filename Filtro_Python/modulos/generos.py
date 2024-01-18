import funciones.corefile as db
import ui.menus as menu
import funciones.reusable as reusable
import modulos.peliculas as controllerPeliculas

local_data = {}

generoInterface = {
    "id": "G01",
    "nombre": "Comedia"
}

def showMenu():
    local_data.update(db.loadData(**db.data))
    while True:
        opcion = input(menu.printMenus("generos"))
        if (opcion == "1"):
            addGenero("")
        elif (opcion == "2"):
            listGeneros()
        elif (opcion == "3"):
            return
        else:
            reusable.printInfo("Error Opcion No Valida....")
        


def addGenero(id):
    pelicula = controllerPeliculas.getPelicula(id)
    if pelicula:
        generos = local_data.get("blockbuster").get("peliculas").get(pelicula["id"]).get("generos")
        while True:
            id = reusable.uuid("generos", list(generos.values()))
            nombre = reusable.checkInput("str", "Ingresa el Nombre del Genero (Comedia, Drama ...)")
            generos.update({
                id:{
                    "id":id, 
                    "nombre":nombre,
                }
            })
            if reusable.breakWhile(f"Se Registro el Genero {nombre} con el ID {id} Correctamente", "Quieres Crear Otro Genero"):
                break
    else:
        return

    db.saveData(**local_data)

def listGeneros():
    pelicula = controllerPeliculas.getPelicula()
    if pelicula:
        generos = local_data.get("blockbuster").get("peliculas").get(pelicula["id"]).get("generos")
        menu.printHeader("lista de generos")
        menu.showDictsInfo(list(generos.values()))
    else:
        return

