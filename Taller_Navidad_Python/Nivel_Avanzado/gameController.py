import campersController as cc
import menusTemplate as menu
import os
import reusable 
import random

novatos = []
intermedio = []
avanzado = []



def runGames():
    while (True):
        os.system("cls")
        print("Empezar Los Juegos de la Categoria")
        opMenu = input(menu.categorias)
        if (opMenu == "1"):
            checkCategory("novatos", novatos)
        elif(opMenu == "2"):
            checkCategory("intermedio", intermedio)
        elif(opMenu == "3"):
            checkCategory("avanzado", avanzado)
        elif(opMenu == "4"):
            break
        else:
            print(menu.error)
        
        os.system("pause")

def listMat(elementos, r, actual=[]):
    if r == 0:
        return [tuple(actual)]
    
    result = []
    for i, elemento in enumerate(elementos):
        result += listMat(elementos[i+1:], r-1, actual + [elemento])
    
    return result


def playMat(jugadores):
    result = listMat(jugadores, 2)
    for i,partido in enumerate(result):
        print(f"Patido Numero {i+1} de la Categoria {partido[0]["categoria"]}")
        print(f"{partido[0]["nombre"]} vs {partido[1]["nombre"]}")
        puntosA = reusable.inputNumber(f"Ingresa Los Puntos de {partido[0]["nombre"]}")
        puntosB = reusable.inputNumber(f"Ingresa Los Puntos de {partido[1]["nombre"]}")
        partido[0]["pj"] += 1
        partido[1]["pj"] += 1
        if puntosA > puntosB:
            pa = (puntosA - puntosB)
            print(f"El Ganador es {partido[0]["nombre"]}")
            partido[0]["pg"] += 1
            partido[1]["pp"] += 1
            partido[0]["pa"] += pa
        elif puntosB > puntosA:
            pa = (puntosB - puntosA)
            print(f"El Ganador es {partido[1]["nombre"]}")
            partido[0]["pp"] += 1
            partido[1]["pg"] += 1
            partido[1]["pa"] += pa
        else:
            print("Empate")

        partido[0]["tp"] += (partido[0]["pg"] * 2)
        partido[1]["tp"] += (partido[1]["pg"] * 2)


def showWiner():
    while (True):
        os.system("cls")
        print("Ver Ganador por Categoria")
        opMenu = input(menu.categorias)
        categoria = ""
        if(opMenu == "1"):
            categoria = "novatos"
            winer = getWiner(novatos)
        elif(opMenu == "2"):
            categoria = "intermedio"
            winer = getWiner(intermedio)
        elif(opMenu == "3"):
            categoria = "avanzado"
            winer = getWiner(avanzado)
        elif(opMenu == "4"):
            break
        else:
            print(menu.error)
        
        if winer:
            print(f"El Ganador de la Categoria {categoria} es {winer["nombre"]}")
            print("Felicidades")

        os.system("pause")


def getWiner(jugadores):
    n = len(jugadores)
    if n:
        mxTP = max(jugador['tp'] for jugador in jugadores)
        winers = [jugador for jugador in jugadores if jugador['tp'] == mxTP]
        if(len(winers) > 1):
            mxPA = max(jugador['pa'] for jugador in winers)
            winers = [jugador for jugador in winers if jugador['pa'] == mxPA]
            if(len(winers) > 1):
                print("Por Decicion de los Juezes el Ganador es")
                return winers[0]
            else:
                return winers[0]
        else:
            return winers[0]
    else:
        print("No se han Jugado los Partidos")
        return False
    

def checkCategory(categoria, jugadores:list):
    cN = len(jugadores)
    if cN:
        print("Esta Categoria ya Jugo")
    else:
        n = []
        for camper in cc.campers:
            if (camper["categoria"] == categoria):
                n .append(camper)

        if (len(n) >= 5):
            jugadores.extend(n)
            playMat(jugadores)
        else:
            jugadores.clear()
            print("No se Pudo Empezar esta Categoria Faltan Participantes")