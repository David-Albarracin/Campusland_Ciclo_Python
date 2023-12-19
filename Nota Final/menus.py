import os

menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante \n4. Mostrar Estudiantes \n5. Salir"
subMenu = "1. Parciales\n2. Quices\n3. Trabajos\n4. Regresar al menu principal"

def principal():
    os.system("cls")
    hasError = True
    print(menu)
    while hasError:
        try:
            hasError = False
            return int(input(":>"))
        except ValueError:
            print("Valor Incorrecto")

def subMenuNotas():
    pass