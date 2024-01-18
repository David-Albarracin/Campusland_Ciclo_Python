import os


headers = {
    "home": "campuslands sistema de notas",
    "registrar": "registar un nuevo camper",
    "areas": "areas disponibles",
    "rutas1": "rutas disponibles",
    "rutaMenu": "Crear o Editar Ruta",
    "jornada": "Selecciona La Jornada ",
    "trainers": "Trainers Disponibles",
    "thematic": "Selecciona Los Temas de Los Modulos",
    "prueba": "Registrar Resultados de Prueba de Admision",
    "matricula": "Matricular Camper",
    "trainer": "Crear Nuevo Trainer",
    "notas": "Selecciona el Modulo",
    "registrarNotas" : "Registrar Notas del Camper",
    "reportes": "Genera pdf con el reporte que quieras",
    "inscrito": "campers con el estado inscrito",
    "aprobado": "campers que aprobaron el examen",
    "bajoRendimiento": "Estudiantes con bajo rendimiento ",
    "infoRutas": "informacion sobre la ruta",
    "eliminarCamper": "Borrar estudiante de la Base de Datos",
    "editarCamper": "Editando Campers"
}


opcions = {
    "home" : [
        "registrar camper",
        "registro de prueba de admision",
        "registro de area de entrenamiento",
        "registro de ruta de entrenamiento",
        "gestionar matricula",
        "registrar notas",
        "registrar nuevo trainer",
        "generar reportes",
        "Eliminar Camper",
        "Editar Camper",
        "salir"
    ],
    "rutaMenu": [
        "Crear Ruta Nueva",
        "Editar Ruta Existente",
        "Salir"
    ],
    "jornada":[
        "mañana",
        "tarde",
    ],
    "trainers":[
        "Crear Nuevo Trainer",
        "Editar Trainer",
        "Salir"
    ],
    "notas":[
        "Fundamentos de Programacion",
        "Programacion WEB",
        "Programacion Formal",
        "Base de Datos",
        "Backend"
    ],
    "reportes":[
        "Listar los campers que se encuentren en estado de inscrito",
        "Listar los campers que aprobaron el examen inicial y no estan Matriculados",
        "Listar los entrenadores que se encuentran trabajando con campuslands",
        "Listar los estudiantes que cuentan con bajo rendimiento.",
        "Listar los campers y entrenador de ruta de entrenamiento",
        "Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos",
        "Salir"
    ]
}



def showMenu(typeMenu):
    showHeader(typeMenu)
    for i, item in enumerate(opcions[typeMenu]):
        print(f" {i+1}.{item.capitalize()}")
    print("")
    return ":> "


def showHeader(typeMenu):
    os.system("cls")
    headerT = f"+  {headers[typeMenu].upper()}  +"
    lenHeader = len(headerT)
    print("+"*lenHeader)
    print(headerT)
    print("+"*lenHeader)
    print("")
    return

