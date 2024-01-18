import funciones.corefile as db
import ui.menus as menu
import funciones.reusable as reusable
import modulos.peliculas as controllerPeliculas

local_data = {}

formatoInterface = {
    "id": "F01",
    "nombre": "DVD",
    "NroCopias": 2,
    "valorPrestamo": 8000
}


def showMenu():
    local_data.update(db.loadData(**db.data))
    while True:
        opcion = input(menu.printMenus("formatos"))
        if (opcion == "1"):
            addFormato("")
        elif (opcion == "2"):
            listFormatos()
        elif (opcion == "3"):
            return
        else:
            reusable.printInfo("Error Opcion No Valida....")
        

def addFormato(id):
    pelicula = controllerPeliculas.getPelicula(id)
    if pelicula:
        formatos = local_data.get("blockbuster").get("peliculas").get(pelicula["id"]).get("formato")
        while True:
            id = reusable.uuid("formatos", list(formatos.values()))
            nombre = reusable.checkInput("str", "Ingresa el Nombre del Formato (DVD, BlueRay ...)")
            NroCopias = reusable.checkInput("int", "Ingrese el Numero de Copias Disponibles")
            valorPrestamo = reusable.checkInput("int", "Ingrese el Valor del Prestamo Por Copia")
            formatos.update({
                id:{
                    "id":id, 
                    "nombre":nombre,
                    "NroCopias": NroCopias,
                    "valorPrestamo": valorPrestamo
                }
            })
            if reusable.breakWhile(f"Se Registro el Formato {nombre} con el ID {id} Correctamente", "Quieres Crear Otro Formato"):
                break
    else:
        return
    
    db.saveData(**local_data)

def listFormatos():
    pelicula = controllerPeliculas.getPelicula()
    if pelicula:
        formatos = local_data.get("blockbuster").get("peliculas").get(pelicula["id"]).get("formato")
        menu.printHeader("lista de formatos")
        menu.showDictsInfo(list(formatos.values()))
    else:
        return