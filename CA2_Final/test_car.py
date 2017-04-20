# Import unit testing framework
import unittest

# Import classes from dealership and car
from dealership import Dealership
from car import Car, Petrol, Diesel, Electric, Hybrid

# Test the functions of the Car class
class Test_Car(unittest.TestCase):
    def setUp(self):
        # Declare an instance of each car type
        self.petrol = Petrol('green', 'VW', 'Golf', 1, 56.0)   
        self.diesel = Diesel('silver', 'Mazda', 'CX-5', 1, 64.0)  
        self.electric = Electric('blue', 'Tesla', 'Model S', 1, 79.0)
        self.hybrid = Hybrid('red', 'Toyota', 'Prius', 1, 45.0)
        
    # Test attribute values
    def test_car_fuel_type_returns_correct_result(self):
        result = self.petrol.fuel_type
        self.assertEqual("petrol", result)
        result = self.diesel.fuel_type
        self.assertEqual("diesel", result)
        result = self.electric.fuel_type
        self.assertEqual("electric", result)
        result = self.hybrid.fuel_type
        self.assertEqual("hybrid", result)
        
    def test_calculate_rental_price_returns_correct_result(self):
        result = self.petrol.calculate_rental_price(7)
        self.assertEqual(result, "Total price: 392.0 euro")
        result = self.petrol.calculate_rental_price('two')
        self.assertEqual(result, "Error! Please enter integer values only.")
        
if __name__=='__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)