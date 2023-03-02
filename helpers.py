import os
import platform
import re

def limpiar_pantalla():      # Función para limpiar la pantalla
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):    #longitud minima y maxima del texto, y mensaje opcional
    print(mensaje) if mensaje else None #si mensaje es None, no se imprime nada, si no, se imprime el mensaje
    while True:   
        texto=input("Introduzca un texto: ")  #leemos el texto
        if len(texto) >= longitud_min and len(texto) <= longitud_max:   #comprobamos que el texto cumple las condiciones y si es asi lo devolvemos
            return texto
