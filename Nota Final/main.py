"""
PROGRAMA PARA CALCULAR LAS NOTAS DE N ESTUDIANTES..
"""
import os
alumnos =[]
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante\n4. Salir\n:)"
subMenuNotas = ["Parciales","Quices","Trabajos","Regresar al menu principal"]
opMenu=0
while (isActive) :
    os.system("cls")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if (opMenu == 1):
            rta = "S"
            while (rta in ["S","s"]):
                codigo = input("Ingrese el Codigo del Estudiante")
                nombre = input("Ingrese el Nombre del Estudiante")
                edad = int(input(f"Ingrese la edad del Estudiante {nombre}"))
                alumno = [codigo,nombre,edad,[],[],[]]
                alumnos.append(alumno)
                os.system("pause")
                rta = input("Desea registrar otro Alumno S(si) o N(No)").upper()
        elif (opMenu == 2):
            opNotas = 0
            isActiveGrades = True
            while (isActiveGrades):
                os.system("cls")
                for i,item in enumerate(subMenuNotas):
                    print(f"{i+1}. {item}")
                try:
                    opNotas = int(input(":)"))
                except ValueError:
                    print("Error en el dato de de ingreso")
                    os.system("pause")
                else:
                    opContinuar = "s"
                    codigo = input("Ingrese el codigo del Estudiante: ")
                    for item in alumnos:
                        if codigo in item:
                            nota = int(input("Ingresa la nota..."))
                            if (opNotas == 1):
                                #3 es Trabajos
                                item[3].append(nota)
                            elif (opNotas == 2):
                                #4 es Quices
                                item[4].append(nota)
                            elif (opNotas == 3):
                                #5 es Parciales
                                item[5].append(nota)
                            elif (opNotas == 4):
                                isActiveGrades = False
                            else:
                                pass
                            opContinuar = input("Desea Ingresar otra nota s / n: >")
                        else:
                            print("Estudiante no encontrado")
                    if (opContinuar not in ["s", "S"]):
                        isActiveGrades = False
                    os.system("pause")
                    
        elif (opMenu == 3):
            codigo = input("Ingrese el codigo del Estudiante: ")
            for item in alumnos:
                if codigo in item:
                    print(item)
            os.system("pause")
        elif (opMenu == 4):
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("Opcion invalida")
    os.system("pause")