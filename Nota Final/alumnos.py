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



def guardarNota(typeNota: str, codigoAlumno: str):
    opContinuar = "s"
    while opContinuar in "Ss":
        alumno = alumnos.get(codigoAlumno)
        notaList = alumno.get("notas").get(typeNota)
        nota = float(input(f"Ingresa la nota Nª{len(notaList) + 1} de {typeNota} para el Estudiante {alumno['nombre']} :> "))
        opContinuar = input(f"Desea Ingresar otra Nota de {typeNota} a {alumno['nombre']} S(si) o N(no) :> ")
        notaList.append(nota)
    
    


def getAlumnoID():
    hasError = True
    while hasError:
        os.system("cls")
        codeAlumno = input("Ingresa el codigo del Estudiante :>")
        data = alumnos.get(codeAlumno, False)
        if data:
            hasError = False
            return data["codigo"]
        else:
            print("Error no encontre este estudiante")
            os.system("pause")



def alumnoPrueba():
    codigo = "123"
    alumno = {
            "codigo": codigo,
            "nombre": "Alumno de Prueba",
            "edad": 10,
            "notas": {
                "parciales": [],
                "quizes": [],
                "trabajos": []
            }
        }
    alumnos.update({codigo:alumno})

def listarAlumnos():
    pass

    #Calcular la nota final, El promedio del Grupo, Cual fue el mejor y el peor 
