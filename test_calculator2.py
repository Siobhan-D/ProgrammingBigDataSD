import unittest

from factorial import factorial
from factorial import factorial_simple

class Conversion(object):

    def lbs_to_kilos(self, lbs):
        return lbs / 2.2

class Calculator(object):

    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def divide(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            if y == 0:
                return 'NaN'
            return x / float(y)
        else:
            raise ValueError

    def exponent(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x ** y
        else:
            raise ValueError

    def multiply(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError

    def subtract(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError

# test the factorial functionality
class TestFactorial(unittest.TestCase):

    # this tests the conversion functionality
    # 5 = 120
    # 6 = 720
    def test_factorial(self):
        result = factorial(5)
        self.assertEqual(120, result)
        result = factorial(6)
        self.assertEqual(720, result)

    # this tests the conversion functionality
    # 5 = 120
    # 6 = 720
    def test_factorial_simple(self):
        result = factorial_simple(5)
        self.assertEqual(120, result)
        result = factorial_simple(6)
        self.assertEqual(720, result)

# test the conversion functionality
class TestConversion(unittest.TestCase):

    def setUp(self):
        self.conversion = Conversion()

    # this tests the conversion functionality
    # 2.2 lbs = 1 kg
    # 22 lbs = 10 kgs
    def test_convert_lbs_to_kilos(self):
        result = self.conversion.lbs_to_kilos(2.2)
        self.assertEqual(1, result)
        result = self.conversion.lbs_to_kilos(22)
        self.assertEqual(10, result)

# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # this tests the add functionality
    # 2 + 2 = 4
    # 2 + 4 = 6
    # 2 + (-2) = 0
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')

    # adding multiplication to my calculator
    def test_calculator_multiply_method_returns_correct_result_for_2_params_the_same(self):
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

    # adding divide to my calculator
    def test_calculator_divide_method_returns_correct_result_for_2_params_the_same(self):
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
        self.assertRaises(ValueError, self.calc.divide, 'two', 'three')
        self.assertRaises(ValueError, self.calc.divide, 'two', 0)
        self.assertRaises(ValueError, self.calc.divide, 2, 'three')

    # adding exponent to my calculator
    def test_calculator_exponent_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2,4)
        self.assertEqual(16, result)
        result = self.calc.exponent(2, -2)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(2, 0)
        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()
