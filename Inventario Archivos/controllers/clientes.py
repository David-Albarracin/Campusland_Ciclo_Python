import controllers.db as db
import templates.menus as menus

#db
db.URL = "/data/db.json"

#TEMPLATES
header = "ADMINISTRACION DE CLIENTES"
opcions = [
    'Nuevo Cliente',
    'Borrar Cliente',
    'Editar Cliente', 
    'Buscar',
    'Menu Principal'
]



def menu():
    while(True):
        op = input(menus.printMenus(header, opcions))
        if(op == "1"):
            cliente = {
                "cc": input("Ingresa la Cedula de Ciudadanida del Cliente :> "),
                "nombre": input("Ingresa el Nombre del Cliente :> ")
            }
            print(cliente)
        elif(op == "5"):
            return
        else:
            print(menus.valueErrorMessage)


def newClient():
    pass