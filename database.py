import csv
import config

class Vehículo:
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

class Coche(Vehículo):
    