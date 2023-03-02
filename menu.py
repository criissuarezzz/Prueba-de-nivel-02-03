import os
import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("=======================")
        print("= Bienvenido al gestor=")
        print("=======================")
        print("Elija que desea hacer: ")
        print("1. Crear vehiculo")
        print("2. Listar vehiculos")
        print("3. Buscar vehiculo")
        print("4. Eliminar vehiculo")
        print("5. Salir")

        opcion = input("Opcion: ")
        helpers.limpiar_pantalla()
    
        if opcion == "1":
            print()
            crear_vehiculo()
        elif opcion == "2":
            listar_vehiculos()
