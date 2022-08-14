import unittest


def es_menor_de_edad (edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristal(unittest.TestCase):
    def test_es_menor_de_edad(self):
        edad = 20
        resultado = es_menor_de_edad(edad)
        self.assertEqual(resultado, True)


if __name__ == '__main__':
    unittest.main()