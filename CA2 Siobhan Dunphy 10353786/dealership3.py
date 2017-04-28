# Assignment 2 
# Angier car rental will rent cars to customers. They have the potential to rent with petrol, diesel
# electric, or hybrid cars.
# They have initially 40 cars in their rental pool made up of 50% petrol, 20% diesel, 10% electric and 20% hybrid.
# When a car is not rented it is available to the customer to rent.
# Once a car is rented the car is assigned to the customer, and removed from the rental pool.
# When the car is returned by the customer it is assigned back into the rental pool.
# If all 40 cars are rented out the rental function should return a message to the customer saying "Sorry nothing 
# to rent, please try again"
# All classes developed should be documented and accompanied by an associated test suite for the classes written.

from car import Car, Petrol, Diesel, Electric, Hybrid 

class Dealership(object):
    def __init__(self, dealership_name):
        self.dealership_name = dealership_name
        #self.total_cars = 0
        self.total_available = 0
        self.available_cars = []
        self.rented_cars = []
        self.cars = ['petrol', 'diesel', 'electric', 'hybrid']
        self.profit = 0
        self.customer = {}
        self.customers = []
    
    def check_total_cars_available(self):
        self.total_available = len(self.available_cars)
        return self.total_available
    
    def check_availability(self, car_type):
        # Go through the inventory and count the number of cars that are available of that type.
        car_type = car_type.lower()
        count = 0
        i=0
        for car in self.available_cars:
            if car.fuel_type == car_type:
                count += 1
        return count  
    
    def car_rental(self, car_type, num_cars, num_days):
        # Check availability of the desired car type and number of cars. Remove the cars from the list and add them to another list.
        total_cost=0.0
        i=0
        car_type = car_type.lower()
        num_available = self.check_availability(car_type)
        self.total_available = self.check_total_cars_available()
        try:  
            num_days = int(num_days)
        except ValueError:
            message = "Invalid input."
            return message
        if car_type in self.cars:
            if num_available >= num_cars:
                for car in self.available_cars:
                    if car.fuel_type == car_type:
                        self.rented_cars.append(self.available_cars.pop(i))
                        #calculate the daily rental price and add to the running daily price
                        cost = car.calculate_rental_price(num_days)
                        total_cost += cost
                        i+=1
                        if i==num_cars:
                            break
                message = "You have successfully rented %s %s cars.\n\nTotal cost: %s euro\n" %(num_cars, car_type, total_cost)
            elif self.total_available==0:
                message = "Sorry, nothing to rent. Please try again."
            else:
                message = "Sorry, only %s %s cars available. Please try again." %(num_available,car_type)
        else:
            message = "Sorry, that type of car is not available."
        self.add_profit(total_cost)
        return message
    
    def add_profit(self, profit):
        self.profit += profit
        return self.profit
        
    def car_return(self, car_type, num_cars):
        i=0
        car_type = car_type.lower()
        for car in self.rented_cars:
            if car.fuel_type == car_type:
                self.available_cars.append(self.rented_cars.pop(i)) 
                i+=1
                if i==num_cars:
                    break
        message = "You have successfully returned %s %s cars." %(num_cars, car_type)
        return message
        
        
        
        