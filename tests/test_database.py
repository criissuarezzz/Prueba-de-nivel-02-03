import copy
import unittest
import csv
import config
import database as db
import helpers

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Vehiculos.lista = [
            db.Coche("rojo", 4, 150, 2000),
            db.Camioneta("blanco", 4, 120, 3000, 1500),
            db.Bicicleta("azul", 2, "urbana"),
            db.Motocicleta("negra", 2, "urbana", 200, 1000),
            db.Vehiculo("verde", 6)]  
    
    def test_catalogar_color(self):
        self.assertEqual(db.Vehiculos.catalogar_color(), "rojo, blanco, azul, negra, verde")
    
    def test_catalogar_ruedas(self):
        self.assertEqual(db.Vehiculos.catalogar_ruedas(), "4, 4, 2, 2, 6")
    
    def test_catalogar_velocidad(self):
        self.assertEqual(db.Vehiculos.catalogar_velocidad(), "150, 120, 200, 200")
    
    def test_catalogar_cilindrada(self):
        self.assertEqual(db.Vehiculos.catalogar_cilindrada(), "2000, 3000, 1000")

    def test_catalogar_carga(self):
        self.assertEqual(db.Vehiculos.catalogar_carga(), "1500")
    
    def test_catalogar_tipo(self):
        self.assertEqual(db.Vehiculos.catalogar_tipo(), "urbana, urbana")
    
    def test_catalogar_vehiculos(self):
        self.assertEqual(db.Vehiculos.catalogar_vehiculos(), "Coche, Camioneta, Bicicleta, Motocicleta, Vehiculo")
    
    def test_listar_vehiculos(self):
        self.assertEqual(db.Vehiculos.listar_vehiculos(), "rojo, 4, 150, 2000, blanco, 4, 120, 3000, 1500, azul, 2, urbana, negra, 2, urbana, 200, 1000, verde, 6")
    
    def test_crear_vehiculo(self):
        self.assertEqual(db.Vehiculos.crear_vehiculo("negro", 4, 200, 3000), "negro, 4, 200, 3000")
        self.assertEqual(db.Vehiculo.crear_vehiculo("verde", 2, "urbana"), "verde", 2, "urbana")

    def test_borrar(self):
        self.assertEqual(db.Vehiculos.borrar(0), "rojo, 4, 150, 2000")
        self.assertEqual(db.Vehiculos.borrar(0), "blanco, 4, 120, 3000, 1500")
        self.assertEqual(db.Vehiculos.borrar(0), "azul, 2, urbana")
        self.assertEqual(db.Vehiculos.borrar(0), "negra, 2, urbana, 200, 1000")
        self.assertEqual(db.Vehiculos.borrar(0), "verde, 6")

