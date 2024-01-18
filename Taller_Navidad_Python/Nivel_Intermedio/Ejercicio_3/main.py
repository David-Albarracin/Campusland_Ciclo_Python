"""
3. En el contexto de la gestión de inventarios, se requiere desarrollar un programa en Python que permita
realizar el control detallado de productos en un negocio. Cada producto estará caracterizado por los siguientes
atributos:
•Código del producto.
•Nombre del producto.
•Valor de compra del producto.
•Valor de venta del producto.
•Stock mínimo permitido.
•Stock máximo permitido.
•Nombre del proveedor del producto.
El programa debe cumplir con las siguientes funcionalidades:
1.Registro de Productos:
1. El usuario podrá registrar nuevos productos proporcionando la siguiente información: código,
nombre, valor de compra, valor de venta, stock mínimo, stock máximo y nombre del
proveedor.

2.Visualización de Productos:
1. El programa deberá permitir la visualización de la lista de productos registrados, mostrando
todos los atributos de cada producto en un formato claro y legible.

3.Actualización de Stock:
1. Se debe implementar la posibilidad de actualizar el stock de un producto específico. El
usuario ingresará el código del producto y la cantidad que desea agregar o restar al stock.

4. Informe de Productos Críticos:
1. El programa deberá generar un informe que muestre los productos cuyo stock
se encuentra por debajo del límite mínimo establecido.

5. Cálculo de Ganancia Potencial:
1. Implementar una función que calcule la ganancia potencial total considerando
la diferencia entre el valor de venta y el valor de compra de cada producto,
multiplicada por la cantidad en stock.
"""

import os
import productosController as pc
import menusTemplate as menu
import reusable

while(True):
    os.system("cls")
    opMenu = input(menu.principal)
    if(opMenu == "1"):
        pc.newProduct()
    elif(opMenu == "2"):
        pc.listProducts()
    elif(opMenu == "3"):
        producto = pc.searchProduct()
        if (producto):
           stock = pc.checkStock(producto['stock_minimo'], producto['stock_maximo'])
           print("Stock Actualizado Correctamente")
    elif(opMenu == "4"):
        pc.criStockList()
    elif(opMenu == "5"):
        pc.bestProduct()
    elif(opMenu == "6"):
        break
    else:
        print("Opcion No Reconocida")

    os.system("pause")