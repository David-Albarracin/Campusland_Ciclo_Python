

import services.corefile as db
import templates.reusable as reusable
import templates.menus as menu

campuslandDB = {
    "areas":{
        "artemis":{
            "nombre": "artemis",
            "morning": [],
            "afternoon": []
        },
        "sputnik":{
            "nombre": "sputnik",
            "morning": ["m1_2"],
            "afternoon": []
        },
        "apolo":{
            "nombre": "apolo",
            "morning": ["j1_1", "j2_1"],
            "afternoon": []
        }
    },

    "rutas": {
        "nodejs":{
            "nombreRuta": "nodejs",
            "area": "sputnik",
            "fechaInicio": "27-11-2023",
            "fechaFinal": "3-6-2024",
            "trainers": ["miguel"],
            "grupos":["m1_2"],
            "jornada": "morning",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["HTML","Bootstrap"],
            "programacionFormal": ["JavaScript", "C#"],
            "basesDatos": ["MongoDB", "MySql"],
            "backend": ["NodeJS", "Express"]
        },
        "java":{
            "nombreRuta": "java",
            "area": "apolo",
            "fechaInicio": "27-11-2023",
            "fechaFinal": "3-6-2024",
            "trainers": ["johlver"],
            "grupos": ["j1_1"],
            "jornada": "morning",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["HTML","CSS"],
            "programacionFormal": ["Java", "C#"],
            "basesDatos": ["Postgresql", "MySql"],
            "backend": ["Spring Boot", "Express"]
        },
        "netcore":{
            "nombreRuta": "netcore",
            "area": "apolo",
            "fechaInicio": "9-1-2024",
            "fechaFinal": "15-7-2024",
            "trainers": ["johlver"],
            "grupos": ["j2_1"],
            "jornada": "morning",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["HTML","CSS"],
            "programacionFormal": ["Java", "C#"],
            "basesDatos": ["Postgresql", "MySql"],
            "backend": ["NetCore", "POO"]
        }
    },

    "trainers":{
        "johlver":{
            "uid": "1",
            "nombre": "johlver",
            "jornada": "morning",
            "grupos": ["j1_1", "j2_1"]
        },
        "miguel":{
            "uid": "2",
            "nombre": "miguel",
            "jornada": "morning",
            "grupos": ["m1_2"]
        }
    },

    "grupos": {
        "j1_1": [],
        "j2_1": [],
        "m1_2": []
    }

}



def newArea():
    loadCampuslanDB()
    menu.showHeader("areas")
    areas = campuslandDB.get("areas")
    reusable.printList(list(areas.keys()))
    opcion = reusable.yesORnot("\nEstas Seguro que Desea Crear Nueva Area de Entrenamiento? ")
    if opcion:
        reusable.showInfo("Por el Momento Campus Solo Cuenta con 3 Areas Asignalas en el Menu de Administrar Rutas")
        """
        nombre = reusable.checkInput("str", "Ingresa el Nombre del Area")
        areas.update({nombre: {"morning": [], "afternoon": []}})
        reusable.showSuccess("Area Creada Correctamente")
        db.newFile(**campuslandDB)
        """
    return

def newRuta():
    loadCampuslanDB()
    menu.showHeader("rutas1")
    rutas = campuslandDB.get("rutas")
    reusable.printList(list(rutas.keys()))
    while(True):
        opcion = input(menu.showMenu("rutaMenu"))
        if(opcion == "1"):
            ruta = {}
            rutaName = reusable.checkInput("str", "Nombre de La Ruta Nueva").replace(" ", "")
            if not (rutaName in rutas):
                ruta.update({"nombreRuta":rutaName})

                print("Fecha de Inicio de La ruta")
                ruta.update({"fechaInicio": reusable.newDate()})
                print("Fecha de Finalizacion de la Ruta")
                ruta.update({"fechaFinal": reusable.newDate()})

                jornada = selectJornada()
                ruta.update({"jornada": jornada})
                
                data = selectTrainer(jornada)
                if data:
                    ruta.update({"trainer": data["trainer"]})

                    grupos = campuslandDB.get("grupos")
                    grupos.update({data["grupo"]:[]})

                    ruta.update({"area":selectArea(jornada, data["grupo"])})

                    menu.showHeader("thematic")
                    ruta.update(selectTematics())
                    
                    rutas.update({rutaName:ruta})
                    db.newFile(**campuslandDB)
                    reusable.showSuccess("Nueva Ruta Creada Correctamente")
                else:
                    reusable.showInfo("Esta Ruta No se Pudo Crear Intentalo de Nuevo mas tarde")


            else:
                reusable.showError("Esa Ruta Ya Existe Intenta con Otro Nombre")
        elif(opcion == "2"):
            reusable.showInfo("Opcion No Disponible por el momento")
        elif(opcion == "3"):
            return
        else:
            reusable.showError("Error Opcion No Reconocida")
    


def selectTrainer(jornada):
    trainers = campuslandDB.get("trainers")
    trainersList = list(trainers.keys())
    while True:
        menu.showHeader("trainers")
        reusable.printList(trainersList)
        nombre = reusable.checkInput("str", "Ingresa el Nombre del Trainer")
        if nombre in trainersList:
            trainer = trainers.get(nombre)
            if trainer["jornada"] == jornada:
                grupos = trainer.get("grupos")
                if len(grupos) < 2: 
                    grupo = f"{trainer['nombre'][0]}{len(grupos)+1}_{trainer['uid']}"
                    grupos.append(grupo)
                    return {"trainer":trainer["nombre"], "grupo":grupo}
                else:
                    reusable.showInfo(f"El Trainer {nombre} No Tiene Disponibilidad Para Mas Grupos")
            else:
                reusable.showInfo(f"El Trainer {nombre} No Tiene Disponibilidad en esa jornada")
        else:
            reusable.showError(f"El Trainer {nombre} No Existe Intentalo de nuevo")

        if not (reusable.yesORnot("Desea Intentar con Otro Trainer")):
            return


def selectArea(jornada, grupo):
    while(True):
        areas = campuslandDB.get("areas")
        menu.showHeader("areas")
        reusable.printList(list(areas.keys()))
        opcion = reusable.checkInput("str", "Ingresa el Nombre del Area")
        if opcion in areas:
            area = areas.get(opcion)
            if (len(area[jornada]) < 2):
                area[jornada].append(grupo)
                return area["nombre"]
            else:
                reusable.showInfo("Esta Area No Cuenta Con Espacio Disponible Intentalo Con Otra o en Jornada Contraria")
        else:
            reusable.showError(f"El Area {opcion} No Existe Intentalo de Nuevo")

def selectJornada():
    while(True):
        opcion = input(menu.showMenu("jornada"))
        if opcion == "1":
            return "morning"
        elif(opcion == "2"):
            return "afternoon"
        else:
            reusable.showError("Opcion No Valida")
        

def selectTematics():
    thematic = {
        "fundamentosProgramacion": [],
        "programacionWEB": [],
        "programacionFormal": [],
        "basesDatos": [],
        "backend": []
    }
    print("Ingresa el Nombre de Los Temas A Tratar en Fundamentos de Programacion")
    print("Temas Recomendados: (Introducción a la algoritmia, PSeInt y Python)")
    thematic["fundamentosProgramacion"].append(reusable.checkInput("str", "Ingresa el Tema Principal"))
    thematic["fundamentosProgramacion"].append(reusable.checkInput("str", "Ingresa el Tema Secundario"))

    print("Ingresa el Nombre de Los Temas A Tratar en Programación Web")
    print("Temas Recomendados: (HTML, CSS y Bootstrap)")
    thematic["programacionWEB"].append(reusable.checkInput("str", "Ingresa el Tema Principal"))
    thematic["programacionWEB"].append(reusable.checkInput("str", "Ingresa el Tema Secundario"))

    print("Ingresa el Nombre de Los Temas A Tratar en Programación formal")
    print("Temas Recomendados: (Java, JavaScript, C#)")
    thematic["programacionFormal"].append(reusable.checkInput("str", "Ingresa el Tema Principal"))
    thematic["programacionFormal"].append(reusable.checkInput("str", "Ingresa el Tema Secundario"))

    print("Ingresa el Nombre de Los Temas A Tratar en Bases de datos")
    print("Temas Recomendados: (Mysql, MongoDb y Postgresql)")
    thematic["basesDatos"].append(reusable.checkInput("str", "Ingresa el Tema Principal"))
    thematic["basesDatos"].append(reusable.checkInput("str", "Ingresa el Tema Secundario"))

    print("Ingresa el Nombre de Los Temas A Tratar en Backend ")
    print("Temas Recomendados: (NetCore, Spring Boot, NodeJS y Express)")
    thematic["backend"].append(reusable.checkInput("str", "Ingresa el Tema Principal"))
    thematic["backend"].append(reusable.checkInput("str", "Ingresa el Tema Secundario"))

    return thematic


def newTrainer():
    loadCampuslanDB()
    trainers = campuslandDB.get("trainers")
    listTrainers = list(trainers.keys())
    menu.showHeader("trainer")
    uid = (len(listTrainers) + 1)
    data = checkTrainer(listTrainers)
    if data:
        trainer = {}
        trainer.update({"nombre": data["nombre"]})
        trainer.update({"uid":uid})
        while  True:
            print("Ingresa La Jornada del Trainer")
            print("1.Mañana")
            print("2.Tarde")
            opcion = reusable.checkInput("str", "")
            if (opcion == "1"):
                jornada = "morning"
                break
            elif(opcion == "2"):
                jornada = "afternoon"
                break
            else:
                reusable.showError("Opcion No Valida")
        
        trainer.update({"jornada":jornada})
        trainer.update({"grupos":[]})
        trainers.update({data["key"]:trainer})
        db.newFile(**campuslandDB)
        reusable.showSuccess("El Trainer Se Registro Correctamente")
    else:
        reusable.showInfo("Este Trainer Ya Existe")
        return

def checkTrainer(listTrainers:list):
    while True:
        nombre = reusable.checkInput("str", "Ingresa el Nombre del Nuevo Trainer")
        nombres = nombre.split(" ")
        for name in nombres:
            if name:
                if not name in listTrainers:
                    return {"key":name, "nombre": nombre}
        
        return

URL = "campusland.json"

def loadCampuslanDB():
    db.URL = URL
    campuslandDB.update(db.checkFile(**campuslandDB))






