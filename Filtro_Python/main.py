import ui.menus as menu
import ui.informes as informes

import modulos.actores as actores
import modulos.formatos as formatos
import modulos.generos as generos
import modulos.peliculas as peliculas

import funciones.reusable as reusable




if __name__ == "__main__":
    while True:
        opcion = input(menu.printMenus("main"))
        if (opcion == "1"):
            generos.showMenu()
        elif (opcion == "2"):
            actores.showMenu()
        elif (opcion == "3"):
            formatos.showMenu()
        elif (opcion == "4"):
            informes.showMenu()
        elif (opcion == "5"):
            peliculas.showMenu()
        elif (opcion == "6"):
            break
        else:
            reusable.printInfo("Erro Opcion No Valida....")