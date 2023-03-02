import csv
import config
import os

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


class Vehiculos():
    lista=[]
    with open(config.VEHÍCULOS.CSV, newline='\n') as csvfile:
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
        
        