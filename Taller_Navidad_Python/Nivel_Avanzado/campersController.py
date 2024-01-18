import reusable
import menusTemplate as menu
import gameController as game
import os

campers = []


def regisCamper():
    camper = {
        "uid": len(campers)+1,
        "nombre": "",
        "edad": "",
        "categoria": "",
        "pj": 0,
        "pg": 0,
        "pp": 0,
        "pa": 0,
        "tp": 0
    }
    camper["nombre"] = reusable.inputString("Ingresa El Nombre del Camper")
    edad = reusable.inputNumber(f"Ingresa la Edad de {camper["nombre"]}")
    if (edad < 15) or (edad > 99):
        print(f"El Camper {camper["nombre"]} no puede participar en el Torneo")
        return
    else:
        camper["edad"] = edad
        while(True):
            os.system("cls")
            print("Registrar Jugador en la Categoria")
            opMenu = input(menu.categorias)
            if(opMenu == "1"):
                if(not len(game.novatos)):
                    if(camper["edad"] == 15) or (camper["edad"] == 16):
                        camper["categoria"] = "novatos"
                        break
                    else:
                        print("la edad para esta categoria es de 15 a 16 años")
                else:
                    print("Los Partidos de esta Categoria ya han Empezado")

            elif(opMenu == "2"):
                if(not len(game.intermedio)):
                    if(camper["edad"] <= 20) and (camper["edad"] > 17):
                        camper["categoria"] = "intermedio"
                        break
                    else:
                        print("la edad para esta categoria es de 17 a 20 años")
                else:
                    print("Los Partidos de esta Categoria ya han Empezado")

            elif(opMenu == "3"):
                if(not len(game.avanzado)):
                    if(camper["edad"] > 20):
                        camper["categoria"] = "avanzado"
                        break
                    else:
                        print("la edad para esta categoria es mayor de 20 años")
                else:
                    print("Los Partidos de esta Categoria ya han Empezado")
            elif(opMenu == "4"):
                break
            else:
                print(menu.error)
            os.system("pause")

    if camper["categoria"]:
        campers.append(camper)
        print(f"Se Registro el Camper {camper["nombre"]} en la Categoria {camper["categoria"]}")


def listJugadores():
    print("{:<10} {:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<10}".format(
    "UID", "Nombre", "", "PJ", "PG", "PP", "PA", "TP"
    ))
    # Línea separadora
    print("="*110)
    # Contenido de la tabla
    for camper in campers:
        print("{:<10} {:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<10}".format(
            camper["uid"],
            camper["nombre"],
            "",
            camper["pj"],
            camper["pg"],
            camper["pp"],
            camper["pa"],
            camper["tp"]
        ))