"""
1. El centro de prevención de sismos en Colombia desea realizar un programa que le permita llevar el
Registro del los sismos presentados en 5 ciudades del país. Por cada ciudad se realizan n cantidad de
Registros. El programa debe permitir registrar las muestras del movimiento en cada ciudad.
Requerimientos:

1. El programa debe tener un menú con las siguientes opciones
1. Registrar Ciudad
2. Registrar Sismo
3. Buscar sismos por ciudad
4. Informe de riesgo
5. Salir

Restricciones:
1. Todas las ciudades deben tener la misma cantidad de sismos registrado
2. El informe de riesgos presenta la siguiente clasificación:
1. Amarillo (Sin riesgo) : El promedio de los sismos es < 2,5
2. Naranja (Riesgo medio) : El promedio de los sismos esta entre 2.6 y 4.5
3. Rojo (Riesgo alto) : El promedio de los sismos es mayor a 4.5
La solución debe implementar listas , listas dentro de listas y modulos

"""

import os 
import ciudadController as cc


while(True):
    os.system("cls")
    print("""
Centro de prevención de sismos en Colombia
    
    1. Registrar Ciudad
    2. Registrar Sismo
    3. Buscar sismos por ciudad
    4. Informe de riesgo
    5. Salir
          
""")
    opMenu = input(":> ")
    if(opMenu == "1"):
        cc.newCity()
    elif(opMenu == "2"):
        ciudad = cc.searchCity()
        if ciudad:
            cc.newSismo(ciudad)
    elif(opMenu == "3"):
        ciudad = cc.searchCity()
        if ciudad:
            print(f"Lista de Sismos de {ciudad[1]} es {ciudad[2]}")
    elif(opMenu == "4"):
        for ciudad in cc.ciudades:
            rango = ciudad[3]
            if (rango < 2.5):
                print(f"{ciudad[1]} : Amarillo (Sin riesgo)")
            elif (rango > 2.6) and (rango <= 4.5):
                print(f"{ciudad[1]} : Naranja (Riesgo medio)")
            elif (rango > 4.5):
                print(f"{ciudad[1]} : Rojo (Riesgo alto)")
    elif(opMenu == "5"):
        break
    else:
        print("Opcion No Reconocida")

    os.system("pause")