import funciones.clientes as c
import os
import json
opciones = ['Gestor clientes','Gestor Proveedores','Gestor Productos','Salir']
opcionClientes = ['Nuevo cliente','Borrar Cliente','Editar Cliente','Buscar','Menu Principal']

def generarMainMenu():
    header="""
    +++++++++++++++++++++++++++++++++
    + SISTEMA GESTOR DE INVENTARIOS +
    +++++++++++++++++++++++++++++++++
    """
    print(header)
    for i,item in enumerate(opciones):
        print(f'{(i+1)} - {item}')
