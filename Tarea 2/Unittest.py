import unittest
from programa import Practica2


class TestStringMethods(unittest.TestCase):


    def saldo(self):
        assert Practica2.sum(50) == 300
        self.assertEqual( Practica2.sum(20), 210)
        
if __name__ == '__main__':
    unittest.main()
    