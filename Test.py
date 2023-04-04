import unittest
from ContadorDePalabras import ContadorDePalabras,frase

class TestContadorDePalabras(unittest.TestCase):

   def test_1 (self):
       
       self.assertEqual(ContadorDePalabras(frase),{
           'hola':1,
           'la':2
       })
    

if __name__ == '__main__':
    unittest.main()