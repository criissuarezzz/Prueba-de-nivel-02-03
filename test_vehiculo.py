import unittest
import config
import vehiculo

class Test_Vehiculo(unittest.TestCase):
    def test_coche(self):
        vehiculo=Vehiculo.Vehículo("rojo", 4)
        self.assertEqual(vehiculo.__str__(), "El color es rojo y tiene 4 ruedas")

    def test_camioneta(self):
        