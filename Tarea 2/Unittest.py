import unittest
import Tarea1


class TestStringMethods(unittest.TestCase):


    def test_sum(self):
        assert Tarea1.sum(20) == 210
        self.assertEqual( Tarea1.sum(20), 210)
        
if __name__ == '__main__':
    unittest.main()