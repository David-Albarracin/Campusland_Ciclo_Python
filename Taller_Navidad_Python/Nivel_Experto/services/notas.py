import services.campers as sc
import services.corefile as db
import templates.reusable as reusable
import templates.menus as menu
import services.campusland as campus


def pruebaAdmision():
    while(True):
        menu.showHeader("prueba")
        camper = sc.getCamper()
        if camper:
            if (camper["estado"] == "inscrito"):
                teorica = reusable.checkInput("float", f"Ingresa la nota de la prueba teorica de {camper["nombre"]}")
                practica = reusable.checkInput("float", f"Ingresa la nota de la prueba practica de {camper["nombre"]}")
                nota = (teorica + practica) / 2
                if (nota >= 60):
                    camper["estado"] = "aprobado"
                else:
                    camper["estado"] = "no_aprobado"

                reusable.showSuccess("Se Actualizo la Nota Correctamente")
                
            elif(camper["estado"] == "no_aprobado"):
                reusable.showInfo(f"El Camper {camper["nombre"]} ya Presento las Pruebas y NO fue apto")
            elif(camper["estado"] == "aprobado"):
                reusable.showInfo(f"El Camper {camper["nombre"]} ya Presento las Pruebas y Aprobo")
            else:
                reusable.showInfo(f"El estado de {camper["nombre"]} no es apto para esta opcion")

        else:
            reusable.showInfo("No se Encontro el Camper")
        
        if(not reusable.yesORnot("Desea Registrar la Nota de otro Camper")):
                db.URL = "campers.json"
                db.newFile(**sc.campers)
                break

def menuNotas():
    while True:
        opcion = input(menu.showMenu("notas"))
        if (opcion == "1"):
            return "moduloFundamentos"
        elif(opcion == "2"):
            return "moduloWEB"
        elif(opcion == "3"):
            return "moduloFormal"
        elif(opcion == "4"):
            return "moduloBaseDatos"
        elif(opcion == "5"):
            return "moduloBackend"
        else:
            reusable.showError("Opcion No Valida Intentalo De Nuevo")

def registrarNotas():
    menu.showHeader("registrarNotas")
    camper = sc.getCamper()
    if camper:
        if camper["estado"] == "estudiando":
            key = menuNotas()
            notas = camper.get("notas")
            if key in list(notas.keys()):
                reusable.showError("Las Notas De Este Modulo Ya se Registraron")
            else:
                notaPruebaTecnica = (reusable.checkInput("float", "Ingresa la Nota de la Prueba Tecnica")*0.6)
                notaPruebaTeorica = (reusable.checkInput("float", "Ingresa la Nota de la Prueba Teorica")*0.3)
                notasTrabajosQuizes = (reusable.checkInput("float", "Ingresa la Definitiva de Trabajos y Quizes")*0.1)
                definitiva = (notaPruebaTecnica + notaPruebaTeorica + notasTrabajosQuizes)
                notas.update({key:{
                    "notaPruebaTecnica": notaPruebaTecnica,
                    "notaPruebaTeorica": notaPruebaTeorica,
                    "notasTrabajosQuizes": notasTrabajosQuizes,
                    "definitiva": definitiva
                }})
                db.URL = sc.URL
                db.newFile(**sc.campers)
                reusable.showSuccess("Se Registraron las Notas Correctamente")
        else:
            reusable.showInfo("El Estado del Camper No es Valido Para Esta Opcion")
    else:
        reusable.showError("No Se Encontro al Camper")

def moduloReportes():
    sc.loadCampers()
    campus.loadCampuslanDB()
    campers = sc.campers
    campuslandDB = campus.campuslandDB
    while True:
        opcion = input(menu.showMenu("reportes"))
        if (opcion == "1"):
            reusable.printList(newReporte("inscrito", campers))
        elif(opcion == "2"):
            reusable.printList(newReporte("aprobado", campers))
        elif(opcion == "3"):
            menu.showHeader("trainers")
            trainers = campuslandDB.get("trainers")
            reusable.printList(list(trainers.keys()))
        elif(opcion == "4"):
            reusable.printList(bajoNotas(campers))
        elif(opcion == "5"):
            menu.showHeader("rutas1")
            rutas = campuslandDB["rutas"]
            reusable.printList(list(rutas.keys()))
            rutaName = reusable.checkInput("str", "Ingresa el Nombre de la Ruta")
            if rutaName in list(rutas.keys()):
                menu.showHeader("infoRutas")
                ruta = rutas[rutaName]
                print(f"Nombre de la Ruta: {ruta["nombreRuta"]}")
                print(f"Trainers de la Ruta: ", end="")
                for trainer in ruta["trainers"]:
                    print(trainer.upper(), end="")
                print("")
                print(f"Campers De la Ruta {ruta["nombreRuta"]}")
                grupos = ruta["grupos"]
                estudiantes = []
                for camper in campers.values():
                    if "grupo" in camper.keys():
                        if (camper["grupo"] in grupos):
                            estudiantes.append(f"CC: {camper['cc']} Nombre: {camper['nombre']}")
                
                if not len(estudiantes):
                    print("No Se Encontraron Campers")

                reusable.printList(estudiantes)
            else:
                print("No se Encontro la ruta a Mostrar")
        elif(opcion == "6"):
            perModul = {}
            pasaron = 0
            perdieron = 0
            for camper in campers.values():
                notas = camper["notas"]
                for key,value in notas.items():
                    nota = value["definitiva"]
                    if nota < 60:
                        perdieron += 1 
                    else:
                        pasaron += 1

                    perModul.update({key: {"pasaron": pasaron, "perdieron":perdieron}})
            message = "Falta Registrar Notas De Algunos Modulos Intentalo de Nuevo mas Tarde"
            for key, value in perModul.items():
                reusable.showSuccess(f"En el Modulo {key} Pasaron:{value["pasaron"]} y Perdieron: {value["perdieron"]}")
                if key == "backend":
                    message = ""
            
            if message:
                reusable.showInfo(message)


        elif(opcion == "7"):
            return
        else:
            reusable.showError("Opcion No Valida Intentalo de Nuevo")


def bajoNotas(campers):
    data = []
    for camper in campers.values():
        notas = camper["notas"]
        for modulo in notas.values():
            nota = modulo["definitiva"]
            if nota < 60:
                data.append(f"CC: {camper['cc']} Nombre: {camper['nombre']}")
    
    menu.showHeader("bajoRendimiento")
    if not len(data):
        print("No Se Encontraron Datos Con esa Caracteristica")

    return data
        

def newReporte(estado, campers:dict):
    if estado:
        menu.showHeader(estado)
        data = []
        for key, value in campers.items():
                if value["estado"] == estado:
                    data.append(f"Nombre del Camper: {value['nombre']}")

    if not len(data):
        print("No Se Encontraron Datos Con esa Caracteristica")

    return data