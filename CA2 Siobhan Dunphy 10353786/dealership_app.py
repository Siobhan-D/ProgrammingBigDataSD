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

from dealership import Dealership
from car import Car, Petrol, Electric, Diesel, Hybrid
from dealership import Dealership
from dealership_view import CarRentalView

from Tkinter import *
import Tkinter as tk

def main():  
    root = tk.Tk()
    root.title("Angier Car Rental")
    root.geometry("600x700")
    app = CarRentalView(root, "Angier Car Rental")
    root.mainloop()  

if __name__ == '__main__':
    main()  