header = "SISTEMA GESTOR DE INVENTARIOS"
opcions = [
    'Gestor Clientes',
    'Gestor Proveedores',
    'Gestor Productos',
    'Salir'
]

valueErrorMessage = "Opcion No Valida.."


def printMenus(header, opcions):
    headerT = f"+ {header} +"
    lenHeader = len(headerT)
    print("+"*lenHeader)
    print(headerT)
    print("+"*lenHeader)
    print("")
    for i, item in enumerate(opcions):
        print(f"{i+1}.{item}")
    print("")
    return ":> "