"""
2. La alcaldía de Bucaramanga desea realizar un programa que le permita calcular el valor de CO2 producido
En las diferentes instalaciones gubernamentales de la ciudad. Tenga en cuenta las siguientes observaciones:

Para calcular el consumo de electricidad, sigue estos pasos:

El programa debe permitir mostrar cual de las instalaciones tiene mayor producción de CO2.
Requerimientos: El programa debe contar con un menú principal que permita realizar todos los
Procesos solicitados.

1. Registrar Dependencia
2. Registrar consumo por dependencia : Tengan en cuenta que se debe registrar los valores
consumidos por los dispositivos en cada una de las oficinas.
3. Ver CO2 producido
4. Dependencia que produce mayor CO2
5. Salir

"""
import os
import dependenciaController as dc


while(True):
    os.system("cls")
    opMenu = input(
"""
Alcaldía de Bucaramanga CO2

    1. Registrar Dependencia
    2. Registrar consumo por dependencia
    3. Ver CO2 producido
    4. Dependencia que produce mayor CO2
    5. Salir

:> """
)
    if(opMenu == "1"):
        dc.newDependencia()
    elif(opMenu == "2"):
        dc.registrarConsumo()
    elif(opMenu == "3"):
        dependencia = dc.searchDependencia()
        if(dependencia):
            print(f"La Dependencia {dependencia['nombre']} tiene un Consumo De {dependencia['CO2']}tCO2eq/MWH")
    elif(opMenu == "4"):
        dependencia = dc.moreCo2()
        print(f"La Dependencia que Produce Mayor C02 es {dependencia['nombre']}")

    elif(opMenu == "5"):
        break
    else:
        print("Opcion No Reconocida")
        
    
    os.system("pause")