# Create an abstract base class object called Car and set initial variables.
from abc import ABCMeta, abstractmethod

class Car(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.colour = " "
        self.make = " "
        self.model = " "
        self.price_per_day = 0.0
    
    def print_make_and_model(self):
        print 'Make: %s\n' %self.make 
        print 'Model: %s\n' %self.model
        return self.make, self.model
    
    def calculate_rental_price(self, days):
        total = days*self.price_per_day  
        return total

# Create child classes for each type of car. 
class Petrol(Car):
    def __init__(self, colour, make, model, price_per_day):
        self.colour = colour
        self.make = make
        self.model = model
        self.price_per_day = price_per_day
        self.fuel_type = 'petrol'
    
class Diesel(Car):
    def __init__(self, colour, make, model, price_per_day):
        self.colour = colour
        self.make = make
        self.model = model
        self.price_per_day = price_per_day
        self.fuel_type = 'diesel'

class Electric(Car):
    def __init__(self, colour, make, model, price_per_day):
        self.colour = colour
        self.make = make
        self.model = model
        self.price_per_day = price_per_day
        self.fuel_type = 'electric'

class Hybrid(Car):
    def __init__(self, colour, make, model, price_per_day):
        self.colour = colour
        self.make = make
        self.model = model
        self.price_per_day = price_per_day
        self.fuel_type = 'hybrid'