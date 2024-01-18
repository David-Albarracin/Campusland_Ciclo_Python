import funciones.corefile as db
import ui.menus as menu
import funciones.reusable as reusable
import modulos.peliculas as controllerPeliculas


local_data = {}

actorInterface = {
    "id": "A01",
    "nombre": "silvester stallone",
    "rol": "protagonista"#| antagonista | reparto
}

actorRoles = {
    "1": "protagonista",
    "2": "antagonista",
    "3": "reparto"
}

def showMenu():
    local_data.update(db.loadData(**db.data))
    while True:
        opcion = input(menu.printMenus("actores"))
        if (opcion == "1"):
            addActor("")
        elif (opcion == "2"):
            listActors()
        elif (opcion == "3"):
            return
        else:
            reusable.printInfo("Error Opcion No Valida....")
        


def addActor(id:str):
    pelicula = controllerPeliculas.getPelicula(id)

    if pelicula:
        actores = local_data.get("blockbuster").get("peliculas").get(pelicula["id"]).get("actores")
        while True:
            id = reusable.uuid("actores", list(actores.values()))
            nombre = reusable.checkInput("str", "Ingresa el Nombre del Actor")
            while True:
                print(f"+ Selecciona el Rol de {nombre} \n")
                for key,value in actorRoles.items():
                    print(f"{key}.{value.capitalize()}")
                print("")
                rolID = reusable.checkInput("str", "")
                if rolID in actorRoles:
                    rol = actorRoles[rolID]
                    break
                else:
                    reusable.printInfo("Ese Rol No Existe Intentalo de Nuevo...")
            
            actores.update({
                id:{
                    "id":id, 
                    "nombre":nombre,
                    "rol": rol
                    }
            })
            if reusable.breakWhile(f"Se Registro el Actor {nombre} con el ID {id} Correctamente", "Quieres Crear Otro Actor"):
                break
    else:
        return
    
    db.saveData(**local_data)

def listActors():
    pelicula = controllerPeliculas.getPelicula()
    if pelicula:
        actores = pelicula.get("actores")
        menu.printHeader("lista de actores")
        menu.showDictsInfo(list(actores.values()))
    else:
        return