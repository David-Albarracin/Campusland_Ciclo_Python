import funciones.corefile as cf
import os
clientes={
}


cf.MY_DATABASE='data/clientes.json'
def NewCustomer(customer : dict):
    clientes.update(customer)
    cf.AddData(customer["cc"],clientes)

def searchCustomer()->dict:
    id=input('Ingrese el Nro Id a Editar :')
    return clientes.get(id,{})

def delCustomer():
    id=input('Ingrese el Nro Id a Borrar :')
    cf.Eliminar(id,clientes)

def modifyCustomer(llave:str,cliente:dict):
    for key,item in cliente.items():
        if ((key != 'edad') and (key != 'cc')):
            if (bool(input(f"Desea editar el campo {key} Enter(Si)")) == False):
                cliente[key]= input(f"Ingrese {key.capitalize()} del cliente : ")
        elif key == 'edad':
            validateAge = True
            while (validateAge):
                try:
                    cliente["edad"]= int(input(f"Ingrese {key.capitalize()}  del cliente : "))
                except ValueError:
                    print("El valor ingresado es invalido")
                else:
                    validateAge = False
    clientes[llave].update(cliente)
    cf.NewFile(clientes)

def validarArchivoClientes():
    if(cf.checkFile()):
        print('ok')
        os.system('pause')
    else:
        cf.NewFile(clientes)