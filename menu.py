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
            print("Has elegido crear un vehiculo")
            print("Cargando...")
            db.Vehiculos.crear()
        elif opcion == "2":
            print("Has elegido listar los vehiculos")
            print("Cargando...")
            db.Vehiculos.listar_vehiculos()
        elif opcion == "3":
            print("Has elegido buscar un vehiculo")
            print("Cargando...")
            print("Qué atributo desea buscar?")
            print("1. Color")
            print("2. Ruedas")
            print("3. Velocidad")
            print("4. Cilindrada")
            print("5. Carga")
            print("6. Tipo")
            opcion = input("Opcion: ")
            if opcion == "1":
                db.Vehiculos.catalogar_color()
            elif opcion == "2":
                db.Vehiculos.catalogar_ruedas()
            elif opcion == "3":
                db.Vehiculos.catalogar_velocidad()
            elif opcion == "4":
                db.Vehiculos.catalogar_cilindrada()
            elif opcion == "5":
                db.Vehiculos.catalogar_carga()
            elif opcion == "6":
                db.Vehiculos.catalogar_tipo()
        elif opcion == "4":
            print("Has elegido eliminar un vehiculo")
            print("Cargando...")
            db.Vehiculos.borrar(helpers.leer_entero(0, len(db.Vehiculos.lista), "Introduzca la posicion del vehiculo que desea eliminar: "))
        elif opcion == "5":
            print("Has elegido salir")
            print("Cargando...")
            break
    
        input("Pulse una tecla para continuar...")



            