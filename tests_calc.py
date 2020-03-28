import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        """Сложение"""
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        """Вычитание"""
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        """Умножение"""
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        """Деление"""
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_oper_neg(self):
        """Негативный, возведение в степень"""
        """ << 22.03.2020   Новык тесты    Павлов А."""
        #self.assertEqual(calc_me(4, 2,"^"), AssertionError)
        self.assertEqual(calc_me(4, 2,"^"), 16)

    
    def test_add_simv1(self):
        """Сложение, первый символ - буква"""
        self.assertEqual(calc_me("j", 2,"+"), "ERROR: now it is does not supported")

    def test_add_simv2(self):
        """Сложение, второй символ - буква"""
        self.assertEqual(calc_me(1, "k","+"), "ERROR: now it is does not supported")

    def test_add_simv_both(self):
        """Сложение, оба символа - буквы"""
        self.assertEqual(calc_me("n", "x","+"), "ERROR: now it is does not supported")

    def test_add_simv_nonum1(self):
        """Сложение, без первого числа"""
        self.assertEqual(calc_me(Null, 2,"+"), "ERROR: send me Number1")   

    def test_add_simv_nonum2(self):
        """Сложение, без второго числа"""
        self.assertEqual(calc_me(4, Null,"+"), "ERROR: send me Number2") 


    """  22.03.2020   Новые тесты    Павлов А. >>  """


if __name__ == '__main__':
    unittest.main(verbosity=2)