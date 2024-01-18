
import random
import reusable
import os

productos = []


def newProduct():
    while(True):
        os.system("cls")
        codigo = random.randint(1000, 9999)
        nombre = input("Ingresa el Nombre del Producto :> ")
        minStock = reusable.inputNumber("Ingresa el Minimo de Stock Permitodo")
        maxStock = reusable.inputNumber("Ingresa el Maximo de Stock Permitodo")
        stock = checkStock(minStock, maxStock)
        valorCompra = reusable.inputFloat("Ingresa el Precio de Compra")
        valorVenta = reusable.inputFloat("Ingresa el Valor de Venta")
        proveedorNombre = input("Ingresa el Nombre del Provedor :> ")
        ganancia = (valorVenta - valorCompra)
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "stock": stock,
            "valor_de_compra": valorCompra,
            "valor_de_venta": valorVenta,
            "stock_minimo": minStock,
            "stock_maximo": maxStock,
            "nombre_del_proveedor": proveedorNombre,
            "ganancia": ganancia
        }
        productos.append(producto)
        os.system("cls")
        print("Producto Creado Correctamente")
        opSubMenu = reusable.yesORnot("¿Desea Registrar Otro Producto?")
        if(not opSubMenu):
            return


def searchProduct():
    while(True):
        nombre = input("Ingresa el Nombre del Producto :> ")
        for producto in productos:
            if (nombre in producto["nombre"]):
                return producto
        print("Producto no Encontrado")
        break


def listProducts():
    """
    for producto in productos:
        for key, value in producto.items():
            key = key.upper().replace("_", " ")
            if ("VALOR" in key) or ("GANANCIA" in key):
                print(f"{key} : ${value}")
            else:
                print(f"{key} : {value}")
    """
    print("{:<10} {:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<20} {:<10}".format(
    "Código", "Nombre", "Stock", "Valor Compra", "Valor Venta", "Stock Mínimo", "Stock Máximo", "Proveedor", "Ganancia"
    ))
    # Línea separadora
    print("="*110)
    # Contenido de la tabla
    for producto in productos:
        print("{:<10} {:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<20} {:<10}".format(
            producto["codigo"],
            producto["nombre"],
            producto["stock"],
            producto["valor_de_compra"],
            producto["valor_de_venta"],
            producto["stock_minimo"],
            producto["stock_maximo"],
            producto["nombre_del_proveedor"],
            producto["ganancia"]
        ))

def bestProduct():
    n = len(productos)
    if n:
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                ganancia_actual = productos[j]['ganancia'] * productos[j]['stock']
                ganancia_siguiente = productos[j + 1]['ganancia'] * productos[j + 1]['stock']

                if ganancia_actual < ganancia_siguiente:
                    # Intercambiar elementos si el producto siguiente tiene una ganancia mayor
                    productos[j], productos[j + 1] = productos[j + 1], productos[j]
        i = 0
        for producto in productos:
            i += 1
            print(f"{i}. {producto['nombre']} ganancia potencial total : ${(producto['ganancia'] * producto['stock'])}")
    else:
        print("No se Encontraron Productos")

def checkStock(minStock, maxStock):
    while(True):
        stock = reusable.inputNumber("Ingresa la Cantidad de Stock Actual")
        if (stock > maxStock):
            print(f"Advertencia : Recuerda que el Stock Maximo Permito es {maxStock}")
        elif(stock < minStock):
            print(f"Advertencia : Recuerda que el Stock Maximo Permito es {maxStock}")

        return stock



def criStockList():
    show = 0
    for product in productos:
        if (product['stock'] < product['stock_minimo']):
            print(f"{product['nombre']} su stock es : {product['stock']} y esta por debajo de {product['stock_minimo']}")
            show += 1
    if not show:
        print("No Se Encontraron Productos en Estado Critico")