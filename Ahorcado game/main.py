#Funciones del Sistema
import os
os.system("cls")

#Vidas que es la bandera para finalizar el juego 
vida = 4
#Palabra adivinar
palabra = "casa"
#Creamos un array para mostrar cuantas letras tiene la palabra
palabra_oculta = ['_'] * len(palabra)
#Creamos un array para ir guardando las letras ingresadas y evitar repetirlas
palabras_ingresadas = []
print("Juego del ahorcado\n")

#Variable que guarda el mensaje final gano | perdio
mensajeFinal = ""

while vida > 0:
  print(f"la palabra adivinar es: {palabra_oculta}\n")
  letra = input("Ingresa una letra: ")
  if (letra in palabras_ingresadas): #Comprobamos si la palabra ya fue ingresada
    os.system("cls")
    print("Ya Ingresaste esa letra\n")
  else:
    palabras_ingresadas.append(letra) #Si no existe la guardamos para saber que ya fue ingresada
    if (letra in palabra):
        for i in range(len(palabra)): #Creamos un ciclo con el rango de palabra este se usa para cambiar el _ por la letra
            if palabra[i] == letra:
                os.system("cls")
                palabra_oculta[i] = letra
                if "_" in palabra_oculta: #Comprobar si todavia existen palabras por adivinar
                    pass
                else:
                    mensajeFinal = "Ganaste Felicidades"
                    vida = 0
    else:
        os.system("cls")
        print(f"La letra {letra} no esta en la palabra")
        vida -= 1
        if vida == 0:#If para evitar mostar el mensaje te quedan 0 vidas
            mensajeFinal = """
                Perdiste
            """
        else:
            print(f"Te quedan {vida} vidas\n")



print(mensajeFinal)