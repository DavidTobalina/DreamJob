import unittest
from calculariva import calculo

class tests_calculariva(unittest.TestCase):
    def test_calculo(self):
        self.assertEqual(calculo(100),21)
if __name__ == '__main__':
    unittest.main()