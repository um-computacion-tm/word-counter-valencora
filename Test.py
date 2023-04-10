import unittest
from ContadorDePalabras import ContadorDePalabras

class TestContadorDePalabras(unittest.TestCase):

   def test_1 (self):
       
       resultado = ContadorDePalabras("hola la la")
       self.assertEqual(resultado,{
           'hola':1,
           'la':2
       })
    

if __name__ == '__main__':
    unittest.main()