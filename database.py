import csv
import config
import os
import helpers
import menu as menu



class Vehiculo():
    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
    def __str__(self):
        return "El color es "+self.color+" y tiene "+str(self.ruedas)+" ruedas"
    def to_dict(self):
        return {
            'color': self.color,
            'ruedas': self.ruedas
        }


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return Vehiculo.__str__(self)+" su velocidad es "+str(self.velocidad)+" su cilindrada es "+str(self.cilindrada)
    def to_dict(self):
        return {
            'velocidad': self.velocidad,
            'cilindrada': self.cilindrada
        }
    
coche=Coche("rojo", 4, 150, 2000)
print(coche)


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga
    def __str__(self):
        return Coche.__str__(self)+" y su carga es "+str(self.carga)
    def to_dict(self):
        return {
            'carga': self.carga
        }
    
camioneta=Camioneta("blanco", 4, 120, 3000, 1500)
print(camioneta)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo
    def __str__(self):
        return Vehiculo.__str__(self)+", su tipo es "+self.tipo
    def to_dict(self):
        return {
            'tipo': self.tipo
        }
    
bicicleta=Bicicleta("azul", 2, "urbana")
print(bicicleta)

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.tipo=tipo
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return Vehiculo.__str__(self)+", su tipo es "+self.tipo+", su velocidad es "+str(self.velocidad)+" y su cilindrada es "+str(self.cilindrada)
    def to_dict(self):
        return {
            'velocidad': self.velocidad,
            'cilindrada': self.cilindrada
        }
moto=Motocicleta("negra", 2, "urbana", 200, 1000)
print(moto)


class Vehiculos:
    lista=[]
    
    with open(config.DATABASE_PATH, newline="\n") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for color, ruedas, velocidad, cilindrada, carga, tipo in reader:
            if velocidad != "":
                lista.append(Camioneta(color, ruedas, velocidad, cilindrada, carga))
            elif ruedas != "":
                lista.append(Vehiculo(color, ruedas))
            elif carga != "":
                lista.append(Coche(color, ruedas, velocidad, cilindrada))
            elif tipo != "":
                lista.append(Motocicleta(color, ruedas, tipo, velocidad, cilindrada))
            elif color != "":
                lista.append(Bicicleta(color, ruedas, tipo))
            elif cilindrada != "":
                lista.append(Camioneta(color, ruedas, velocidad, cilindrada, carga))

        @staticmethod
        def catalogar_ruedas(ruedas):
            for vehiculo in Vehiculos.lista:
                if vehiculo.ruedas == ruedas:
                    print(vehiculo)

        @staticmethod
        def catalogar_color(color):
            for vehiculo in Vehiculos.lista:
                if vehiculo.color == color:
                    print(vehiculo)
        
        @staticmethod
        def catalogar_cilindrada(cilindrada):
            for vehiculo in Vehiculos.lista:
                if vehiculo.cilindrada == cilindrada:
                    print(vehiculo)
        
        @staticmethod
        def catalogar_carga(carga):
            for vehiculo in Vehiculos.lista:
                if vehiculo.carga == carga:
                    print(vehiculo)
        
        @staticmethod
        def catalogar_tipo(tipo):
            for vehiculo in Vehiculos.lista:
                tipo.lower()
                if vehiculo.tipo == tipo:
                    print(vehiculo)
        
        @staticmethod
        def catalogar_velocidad(velocidad):
            for vehiculo in Vehiculos.lista:
                if vehiculo.velocidad == velocidad:
                    print(vehiculo)
        
        @staticmethod
        def listar_vehiculos():
            for vehiculo in Vehiculos.lista:
                print(vehiculo)

        @staticmethod
        def crear():
            color=input("Introduce el color del vehículo: ").lower()
            ruedas=int(input("Introduce el número de ruedas del vehículo: "))
            opcion=input("¿quieres dejarlo como vehículo?(s/n):").lower()
            if opcion == "s":
                print("Guardado como vehículo con "+str(ruedas)+" ruedas y color "+color+".")
                Vehiculos.lista.append(Vehiculo(color, ruedas))
                print(input("Pulse enter para continuar:"))
                if input == "":
                    os.system("cls")
                    return menu.inicio()
            elif opcion == "n":
                if ruedas == 4:
                    velocidad=int(input("Introduce la velocidad del vehículo: "))
                    cilindrada=int(input("Introduce la cilindrada del vehículo: "))
                    print(input("Si lo dejas así será un coche,¿quieres que sea una camioneta?(s/n)"))
                    if input == "s":
                        carga=int(input("Introduce la carga del vehículo: "))
                        print("Guardado como camioneta con "+str(ruedas)+" ruedas, color "+color+", velocidad "+str(velocidad)+", cilindrada "+str(cilindrada)+" y carga "+str(carga)+".")
                        Vehiculos.lista.append(Camioneta(color, ruedas, velocidad, cilindrada, carga))
                        print(input("Pulse enter para continuar:"))
                        if input == "":
                            os.system("cls")
                            return menu.inicio()
                    elif input == "n":
                        print("Guardado como coche con "+str(ruedas)+" ruedas, color "+color+", velocidad "+str(velocidad)+" y cilindrada "+str(cilindrada)+".")
                        Vehiculos.lista.append(Coche(color, ruedas, velocidad, cilindrada))
                        print(input("Pulse enter para continuar:"))
                        if input == "":
                            os.system("cls")
                            return menu.inicio()
                elif ruedas == 2:
                        tipo=input("Introduce el tipo del vehículo(urbana o deportiva): ")
                        print(input("Si lo dejas así será una bicicleta,¿quieres que sea una motocicleta?(s/n)"))
                        if input == "s":
                            velocidad=int(input("Introduce la velocidad del vehículo: "))
                            cilindrada=int(input("Introduce la cilindrada del vehículo: "))
                            Vehiculos.lista.append(Motocicleta(color, ruedas, tipo, velocidad, cilindrada))
                            print("Guardado como motocicleta con "+str(ruedas)+" ruedas, color "+color+", tipo "+tipo+", velocidad "+str(velocidad)+" y cilindrada "+str(cilindrada)+".")
                            print(input("Pulse enter para continuar:"))
                            if input == "":
                                os.system("cls")
                                return menu.inicio()
                        elif input == "n":
                            Vehiculos.lista.append(Bicicleta(color, ruedas, tipo))
                            print("Guardado como bicicleta con "+str(ruedas)+" ruedas, color "+color+" y tipo "+tipo+".")
                            print(input("Pulse enter para continuar:"))
                            if input == "":
                                os.system("cls")
                                return menu.inicio()
            Vehiculos.crear()
           
        
        @staticmethod
        def borrar(posicion):
            posicion=int(input("Introduce la posición del vehículo que quieres borrar: "))
            Vehiculos.lista.pop(posicion)
            Vehiculos.crear()