import controllers.db as db
import templates.menus as menus
import controllers.reusable as reusable

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

cliente = {
    "cc": "",
    "nombre": "",
    "apellidos": "",
    "email_personal": "",
    "email_empresarial": "",
    "edad": 0,
    "telefonos": []
}



def menu():
    while(True):
        op = input(menus.printMenus(header, opcions))
        if(op == "1"):
            for key, value in cliente.items():
                cliente[key] = input(f"Ingresa {key.upper()} del Cliente")
                if type(value) == int:
                    cliente[key] = reusable.checkInput("int",f"Ingresa {key.upper()} del Cliente")
                elif type(value) == list:
                    pass
        elif(op == "5"):
            return
        else:
            print(menus.valueErrorMessage)


def newClient():
    pass