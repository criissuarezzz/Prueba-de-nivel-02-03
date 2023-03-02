class Vehículo():
    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
    def __str__(self):
        return "El color es "+self.color+" y tiene "+str(self.ruedas)+" ruedas"
    
class Coche(Vehículo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return Vehículo.__str__(self)+" y su velocidad es "+str(self.velocidad)+" y su cilindrada es "+str(self.cilindrada)
    
coche=Coche("rojo", 4, 150, 2000)
print(coche)

class Camioneta(Coche):
    