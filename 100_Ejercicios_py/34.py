"""
Calcula las ganancias de una Garita de Control, con cada vehículo que pasa.
"""

#importamos el modulo de codigo reusable mas info en reusable.py
import reusable


run = True

importe = {
    "turnoMañana": 0,
    "turnoNoche": 0,
    "importeOnimus": 0,
    "importeMinivan": 0,
    "importeMicro": 0
}


while(run):
    print(
        """
TIPO DE VEHICULO

    1. Omnibus
    2. Minivan
    3. Micro
    4. Salir

    """
    )
    menuOpcion = reusable.inputNumber("")
    tarifa = 0
    if (menuOpcion == 1):
        tarifa = 5
        importe["importeOnimus"] +=  tarifa
    elif(menuOpcion == 2):
        tarifa = 10
        importe["importeMinivan"] +=  tarifa
    elif(menuOpcion == 3):
        tarifa = 8
        importe["importeMicro"] +=  tarifa
    elif(menuOpcion == 4):
        run = False
    else:
        print("No Conosco esa Opcion")
    
    turno = input("Ingresa el Turno (M/N) :> ").upper()
    
    if (turno == "M"):
        importe["turnoMañana"] +=  tarifa
    else:
        importe["turnoNoche"] +=  tarifa

print(f"Turno de La Mañana : {importe['turnoMañana']}")
print(f"Turno de La Noche : {importe['turnoNoche']}")

print(f"Importe de Ohmibus : {importe['importeOnimus']}")
print(f"Importe de Minivan : {importe['importeMinivan']}")
print(f"Importe de Micro : {importe['importeMicro']}")
