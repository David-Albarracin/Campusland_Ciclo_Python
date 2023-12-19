import os

alumnos = {}

def newAlumno():
    hasError = True
    while hasError:
        os.system("cls")
        codigo = input("Ingresa el codigo del Estudiante :> ")
        nombre = input("Ingresa el Nombre del Estudiante :> ")
        edad = input("Ingresa la Edad del Estudiante :> ")
        alumno = {
            "codigo": codigo,
            "nombre": nombre,
            "edad": edad,
            "notas": {
                "parciales": [],
                "quizes": [],
                "trabajos": []
            }
        }
        if (codigo in alumnos):
            os.system("cls")
            print("Este Alumno ya Existe")
            os.system("pause")
        else:
            alumnos.update({codigo:alumno})
            if "S" not in input(("\nSe Creo el Alumno Correctamente\nDesea Crear Otro Alumno? S/N :>")).upper():
                hasError = False

def buscarAlumno():
    os.system("cls")
    codigo = input("Ingrese el codigo del Estudiante :>")
    alumno = alumnos.get(codigo, {"Error 404": "Alumno no Encontrado"})
    for key,valor in alumno.items():
            print (f"{key}: {valor}")

    os.system("pause")