import unittest

def suma(num1, num2): 
    return abs(num1) + num2

class cajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 10
        nume_2 = 5

        resultado = suma(nume_2, num_1)
        self.assertEqual(resultado, 15)
    def test_suma_dos_negativos(self):
        num1 = -10
        num2 = -7
        retultado = suma(num1, num2)
        self.assertEqual(retultado, -17)

if __name__ == '__main__':
    unittest.main()