import unittest
from calculator_lists import CalculatorList

# test the calculator functionality with lists
class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Declare instance of calculator.
        self.calc = CalculatorList()
        self.list = [1,2,3,4]
    
    # Test the add function.
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(self.list)
        self.assertEqual(10, result)
        result = self.calc.add(nums = [-2,2,0])
        self.assertEqual(0, result)
        result = self.calc.add(-4, -2)
        self.assertEqual(-6, result)

if __name__ == '__main__':
    unittest.main()
