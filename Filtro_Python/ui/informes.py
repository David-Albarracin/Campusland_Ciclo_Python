import funciones.corefile as db
import ui.menus as menu
import funciones.reusable as reusable
import os

local_data = {}

def showMenu():
    local_data.update(db.loadData(**db.data))
    while True:
        opcion = input(menu.printMenus("informes"))
        if (opcion == "1"):
            listPeliculasPerGenero()
            os.system("pause")
        elif (opcion == "2"):
            silvesterGood()
            os.system("pause")
        elif (opcion == "3"):
            showInfoPelicula()
            os.system("pause")
        elif (opcion == "4"):
            return
        else:
            reusable.printInfo("Error Opcion No Valida....")
        


def listPeliculasPerGenero():
    genero = reusable.checkInput("str", "Ingresa el Genero")
    peliculas = local_data.get("blockbuster").get("peliculas")
    if peliculas:
        menu.showDictsInfo(reusable.filterFor("genero", genero, **peliculas))
    else:
        reusable.printInfo("Sin Datos Para Mostrar")

def silvesterGood():
    peliculas = local_data.get("blockbuster").get("peliculas")
    data = []
    if peliculas:
        for pelicula in peliculas:
            if ((pelicula["actores"]["nombre"] == "silvester stallone") and (pelicula["actores"]["rol"] == "protagonista")):
                data.append(pelicula["id"])

        print(data)
        print("")
    else:
        reusable.printInfo("Sin Datos Para Mostrar")

def showInfoPelicula():
    peliculas = local_data.get("blockbuster").get("peliculas")
    if peliculas:
        for pelicula in peliculas:
            print(f"{pelicula['sinopsis']}")
            print(f"{pelicula['actores']}")
            print("")
    else:
        reusable.printInfo("Sin Datos Para Mostrar")

