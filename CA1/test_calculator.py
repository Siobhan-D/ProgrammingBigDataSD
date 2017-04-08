import unittest
from calculator import Calculator

# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
        # declare instance of calculator
        self.calc = Calculator()

    # this tests the add functionality
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)
    
    # this tests the subtract functionality
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)
    
    # tests multiply functionality
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2,4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2, -2)
        self.assertEqual(-4, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)

    # test divide functionality
    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(4,2)
        self.assertEqual(2, result)
        result = self.calc.divide(2, -2)
        self.assertEqual(-1, result)
        result = self.calc.divide(2, 4)
        self.assertEqual(0.5, result)
        result = self.calc.divide(2, 0)
        self.assertEqual('NaN', result)

    # test power functionality
    def test_calculator_power_method_returns_correct_result(self):
        result = self.calc.power(2,2)
        self.assertEqual(4, result)
        result = self.calc.power(-2,4)
        self.assertEqual(16, result)
        result = self.calc.power(2,-2)
        self.assertEqual(0.25, result)
        result = self.calc.power(2,0)
        self.assertEqual(1, result)
    
    # test square functionality
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square(2)
        self.assertEqual(4, result)
        result = self.calc.square(-4)
        self.assertEqual(16, result)
        result = self.calc.square(0.5)
        self.assertEqual(0.25, result)
        result = self.calc.square(0)
        self.assertEqual(0, result)

    # test sin functionality
    def test_calculator_sin_func_method_returns_correct_result(self):
        result = round(self.calc.sin_func(140),4)
        self.assertEqual(0.9802, result)
        result = round(self.calc.sin_func(270),4)
        self.assertEqual(-0.176, result)
        result = round(self.calc.sin_func(-90),4)
        self.assertEqual(-0.8940, result)
        result = round(self.calc.sin_func(0),4)
        self.assertEqual(0, result)
    
    # test cos functionality
    def test_calculator_cos_func_method_returns_correct_result(self):
        result = round(self.calc.cos_func(140),4)
        self.assertEqual(-0.1978, result)
        result = round(self.calc.cos_func(270),4)
        self.assertEqual(0.9844, result)
        result = round(self.calc.cos_func(-90),4)
        self.assertEqual(-0.4481, result)
        result = round(self.calc.cos_func(0),4)
        self.assertEqual(1, result)
     
    # test tan functionality
    def test_calculator_tan_func_method_returns_correct_result(self):
        result = round(self.calc.tan_func(135),4)
        self.assertEqual(-0.0887, result)
        result = round(self.calc.tan_func(270),4)
        self.assertEqual(-0.1788, result)
        result = round(self.calc.tan_func(-90),4)
        self.assertEqual(1.9952, result)
        result = round(self.calc.tan_func(0),4)
        self.assertEqual(0, result)
        
    # test log functionality
    def test_calculator_logarithm_method_returns_correct_result(self):
        result = round(self.calc.logarithm(56),4)
        self.assertEqual(1.7482, result)
        result = round(self.calc.logarithm(2),4)
        self.assertEqual(0.301, result)
        result = self.calc.logarithm(0)
        self.assertEqual('NaN', result)
        result = self.calc.logarithm(-5)
        self.assertEqual('NaN', result)   
        
if __name__ == '__main__':
    unittest.main()
