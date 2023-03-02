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

class Vehículos:
    def __init__(self):
        self.vehículos = []
    
    def add(self, vehículo):
        self.vehículos.append(vehículo)
    
    def __iter__(self):
        return iter(self.vehículos)
    
    def __str__(self):
        return str(self.vehículos)
    
    def to_dict(self):
        return [vehículo.to_dict() for vehículo in self.vehículos]
    
    def to_csv(self):
        with open(config.VEHÍCULOS.CSV, 'w', newline='') as csvfile:
            fieldnames = ['color', 'ruedas']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for vehículo in self.vehículos:
                writer.writerow(vehículo.to_dict())
        
