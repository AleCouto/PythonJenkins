import unittest
import Calculadora


class TestCalculadora(unittest.TestCase):
    def teste_adiciona_inteiros(self):
        resultado = Calculadora.add(2,2)
        self.assertEqual(resultado,4)

    def teste_adiciona_decimais(self):
        resultado = Calculadora.add(5.3,2)
        self.assertEqual(resultado,7.3)

    def teste_adiciona_string_inteiro(self):
        resultado = Calculadora.add('alexandre',2)
        self.assertEqual(resultado,'alexandre2')

    def teste_adiciona_string_decimal(self):
        resultado = Calculadora.add('alexandre',2.2)
        self.assertEqual(resultado,'alexandre2.2')

    def teste_adiciona_string(self):
        resultado = Calculadora.add('alexandre','couto')
        self.assertEqual(resultado,'alexandre couto')

    if __name__ == "__name__":
        unittest.main()

    