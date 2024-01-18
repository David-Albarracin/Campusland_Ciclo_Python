import os

headers = {
    "main": "sistema gestor de peliculas blockbuster",
    "generos": "gestor de generos",
    "actores": "gestor de actores",
    "formatos": "gestor de formatos",
    "peliculas": "gestor de peliculas",
    "informes": "gestor de informes"
}


opcions = {
    "main": [
        "administrador de generos",
        "administrador de actores",
        "administrador de formatos",
        "gestor de informes",
        "gestor peliculas",
        "salir"
    ],
    "generos": [
        "crear genero",
        "listar generos",
        "ir menu principal"
    ],
    "actores": [
        "crear actor",
        "listar actores",
        "ir menu principal"
    ],
    "formatos": [
        "crear formatos",
        "listar formatos",
        "ir menu principal"
    ],
    "peliculas": [
        "agregar pelicula",
        "editar pelicula",
        "eliminar pelicula",
        "buscar pelicula",
        "listar todas las peliculas",
        "ir menu principal"
    ],
    "informes": [
        "listar las peliculas de un genero especifico",
        "listar las peliculas donde el protagonista sea silvester stallone",
        "buscar peliculas y mostrar la sinopsis y los actores",
        "ir menu principal"
    ]

}



def printHeader(message:str):
    os.system("cls")
    message = f"+   {message.upper()}   +"
    caracter = "+"*len(message)
    print(caracter)
    print(message)
    print(caracter)
    print("")

def printMenus(keyMenu):
    printHeader(headers[keyMenu])
    for i,opcion in enumerate(opcions[keyMenu]):
        print(f"{i+1}.{opcion.capitalize()}")
    print("")
    return ":> "


def showDictsInfo(arrayDicts:list):
    for dicc in arrayDicts:
        for key, value in dicc.items():
            if type(value) == "str":
                print(f"{key.capitalize()}: {value.capitalize()}")
            else:
                print(f"{key.capitalize()}: {value}")
        print("")

    os.system("pause")