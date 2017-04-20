# Import unit testing framework
import unittest

# Import classes from dealership and car
from dealership import Dealership
from car import Car, Petrol, Diesel, Electric, Hybrid 

# Test the functions of the Dealership class
class Test_Dealership(unittest.TestCase):
    def setUp(self):
        # Declare an instance of a vehicle   
        self.dealer = Dealership('Some Dealership')
        
        for i in range(20):
            self.dealer.available_cars.append(Petrol('green', 'VW', 'Golf', 56.0))
    
        for i in range(8):
            self.dealer.available_cars.append(Diesel('silver', 'Mazda', 'CX-5', 64.0))

        for i in range(4):
            self.dealer.available_cars.append(Electric('blue', 'Tesla', 'Model S', 79.0))

        for i in range(8):
            self.dealer.available_cars.append(Hybrid('red', 'Toyota', 'Prius', 45.0))
    
        self.dealer.car_rental('petrol', 1, 2)
    
    def test_check_total_cars_available_returns_correct_result(self):
        result = self.dealer.check_total_cars_available()
        self.assertEqual(result, 39)
        
    def test_check_availability_function_returns_correct_result(self):
        result = self.dealer.check_availability('electric')
        self.assertEqual(result, 4)
        
    def test_car_rental_function_returns_correct_result(self):
        result = self.dealer.car_rental('hybrid', 2, 2)
        self.assertEqual(result, "You have successfully rented 2 hybrid cars.\n\nTotal cost: 180.0 euro")
        result = self.dealer.car_rental('Petrol', 1, 5)
        self.assertEqual(result, "You have successfully rented 1 petrol cars.\n\nTotal cost: 280.0 euro")
        result = self.dealer.car_rental('electric', 8, 1)
        self.assertEqual(result, "Sorry, only 4 electric cars available. Please try again.")
        result = self.dealer.car_rental('motorcycle', 1, 8)
        self.assertEqual(result, "Sorry, that car type is not available at this dealership.")
        result = self.dealer.car_rental('petrol', 'three', 3)
        self.assertEqual(result, "Error! Please enter integer values only.")

    def test_car_return_function_returns_correct_result(self):
        result = self.dealer.car_return('hybrid', 8)
        self.assertEqual(result, "Sorry, we have no record of your car rental.")
        result = self.dealer.car_return('Petrol', 1)
        self.assertEqual(result, "You have successfully returned 1 petrol cars.")
        result = self.dealer.car_return('petrol', 'three')
        self.assertEqual(result, "Error! Please enter integer values only.")

if __name__ == '__main__': unittest.main()