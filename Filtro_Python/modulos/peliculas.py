import funciones.corefile as db
import ui.menus as menu
import funciones.reusable as reusable
import modulos.actores as controllerActores
import modulos.formatos as controllerFormatos
import modulos.generos as controllerGeneros

local_data = {}

peliculaInterface = {
    "id": "P01",
    "nombre": "Rambo",
    "duracion": 80,
    "sinopsis": "10 de enero a las dos de la mañana era un dia",
    "generos": {},
    "actores": {},
    "formatos": {}
}

def showMenu():
    local_data.update(db.loadData(**db.data))
    while True:
        opcion = input(menu.printMenus("peliculas"))
        if (opcion == "1"):
            addPelicula()
        elif (opcion == "2"):
            editPelicula()
        elif (opcion == "3"):
            delPelicula()
        elif (opcion == "4"):
            searchPelicula()
        elif (opcion == "5"):
            listPeliculas()
        elif (opcion == "6"):
            return
        


def addPelicula():
    peliculas = local_data.get("blockbuster").get("peliculas")
    while True:
        id = reusable.uuid("peliculas", list(peliculas.values()))
        nombre = reusable.checkInput("str", "Ingresa el Nombre de la Pelicula")
        duracion = reusable.checkInput("int", "Ingresa la Duracion de La Pelicula en Minutos")
        sinopsis = reusable.checkInput("str", "Ingresa la Sinopsis de la pelicula")
        peliculas.update({
            id:{
                "id":id, 
                "nombre":nombre,
                "duracion": duracion,
                "sinopsis": sinopsis,
                "actores": {},
                "generos": {},
                "formato": {}
            }
        })
        db.saveData(**local_data)
        controllerActores.addActor(id)
        controllerGeneros.addGenero(id)
        controllerFormatos.addFormato(id)
        if reusable.breakWhile(f"Se Registro La Pelicula {nombre} con el ID {id} Correctamente", "Quieres Crear Otra Pelicula"):
            break

    db.saveData(**local_data)

def searchPelicula():
    pelicula = getPelicula(id)
    if pelicula:
        print(f"Se encontro la pelicula con el id {pelicula["id"]}")

def delPelicula():
    peliculas = local_data.get("blockbuster").get("peliculas")
    pelicula = getPelicula(id)
    if pelicula:
        peliculas.pop(pelicula["id"])
        db.saveData(**local_data)


def getPelicula(id):
    local_data.update(db.loadData(**db.data))
    if id:
        peliculas = local_data.get("blockbuster").get("peliculas")
        return peliculas.get(id)
    else:
        while True:
            peliculas = local_data.get("blockbuster").get("peliculas")
            peliculaID = reusable.checkInput("str", "Ingresa el ID de la Pelicula")
            if peliculaID in peliculas:
                return peliculas.get(peliculaID)
            else:
                if reusable.breakWhile("No se Encontro Esa Pelicula", "Desea Intentar con Otra"):
                    return



def editPelicula():
    pelicula = getPelicula(id)
    if pelicula:
        for key, value in pelicula.items():
            if value == "dict":
                pass
            else:
                if (reusable.breakWhile(f"Desea Editar {key}: {value}", "")):
                    pass
                else:
                    pelicula[key] = reusable.checkInput(type(value), "Ingresa {key}")


def listPeliculas():
    peliculas = local_data.get("blockbuster").get("peliculas").keys()
    if peliculas:
        for i in peliculas:
            print(f"{i}")
    else:
        reusable.printInfo("No se Encontraron Peliculas")
    