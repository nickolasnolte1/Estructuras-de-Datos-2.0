import unittest
import Practica2


class TestStringMethods(unittest.TestCase):


    def agregar_debitos(self):
        assert Practica2.sum(50) == 300
        self.assertEqual( Practica2.sum(20), 210)
        
if __name__ == '__main__':
    unittest.main()