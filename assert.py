import unittest

def Perkalian(bilangan1, bilangan2):
    return bilangan1 * bilangan2

class SimpleTest(unittest.TestCase):
    def testPerkalian(self):
        input_bilangan1 = float(input("Masukkan bilangan 1: "))
        input_bilangan2 = float(input("Masukkan bilangan 2: "))
        input_perkiraan = float(input("Masukkan perkiraan hasil dari bilangan yang anda masukkan: "))
        self.assertEquals(Perkalian(input_bilangan1, input_bilangan2), input_perkiraan)

if __name__ == '__main__':
    unittest.main()

