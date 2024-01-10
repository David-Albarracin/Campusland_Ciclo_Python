import funciones.clientes as c
import os
import json
opcionClientes = ['Nuevo cliente','Borrar Cliente','Editar Cliente','Buscar','Menu Principal']

def generarClienteMenu():
    c.cf.checkFile(c.clientes) #Invocar metodo para verificar si existe file
    isActiveCustomer = True
    header="""
    +++++++++++++++++++++++++++++++++
    +   ADMINISTRACION DE CLIENTES  +
    +++++++++++++++++++++++++++++++++
    """
    while (isActiveCustomer):
        os.system('cls')
        print(header)
        for i,item in enumerate(opcionClientes):
            print(f'{(i+1)} - {item}')
        try:
            op = int(input(":)_"))
        except ValueError:
            print("Error en el tipo de dato")
        else:
            if(op == 1) :
                os.system('cls')
                title = """
                +++++++++++++++++++++++++++++++++++++++
                +      CREACION DE NUEVO CLIENTE      +
                +++++++++++++++++++++++++++++++++++++++
                """
                print(title)
                cliente={
                    'cc':'00',
                    'nombre':'',
                    'apellidos':'',
                    'emailpersonal':'',
                    'emailcorporativo':'',
                    'edad':0 
                }
                for key,item in cliente.items():
                    if (key != 'edad'):
                        cliente[key]= input(f"Ingrese {key.capitalize()} del cliente : ")
                    else:
                        validateAge = True
                        while (validateAge):
                            try:
                                cliente["edad"]= int(input(f"Ingrese {key.capitalize()}  del cliente : "))
                            except ValueError:
                                print("El valor ingresado es invalido")
                            else:
                                validateAge = False
                isAddPhone = True
                telefono={
                    'telefono':[]
                }
                phone ={
                    "titulo" : 'xx',
                    "valor" : '000'
                }
                os.system('cls')
                msgPhone = """
                +++++++++++++++++++++++++++++++++++++
                +       INFORMACION DE CONTACTO     +
                +++++++++++++++++++++++++++++++++++++
                """
                print(msgPhone)
                while (isAddPhone):
                    phone["titulo"] = input("Ingrese ubicacion (Casa,Oficina,Movil) : ")
                    phone["valor"] = input(f'Ingrese el Nro {phone["titulo"]} del cliente {cliente["nombre"]} :')
                    telefono["telefono"].append(phone)
                    isAddPhone=bool(input("Para terminar presione Enter.... o Cualquier letra para continuar"))
                cliente.update(telefono)
                c.NewCustomer(cliente)
            elif (op == 2) :
                c.delCustomer()
            elif (op == 3) :
                os.system('cls')
                title = """
                +++++++++++++++++++++++++++++++++++++++
                +           EDICION DE CLIENTES       +
                +++++++++++++++++++++++++++++++++++++++
                """
                data = c.searchCustomer()
                if(len(data)):
                    c.modifyCustomer(data["cc"],data)
            elif (op == 4) :
                pass
            elif (op == 5) :
                isActiveCustomer = False
