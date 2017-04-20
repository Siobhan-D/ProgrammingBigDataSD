from dealership import Dealership
from car import Car, Petrol, Diesel, Hybrid, 
from dealership_view import CarRentalView

from Tkinter import *
import Tkinter as tk

# Create an instance of Dealership
dealer = Dealership('Aungier Car Rental', 40, 40)

# Add cars to the available_cars list in the newly created dealership instance
for i in range(20):
    dealer.available_cars.append(Petrol('green', 'VW', 'Golf', 1, 56.0))
    
for i in range(8):
    dealer.available_cars.append(Diesel('silver', 'Mazda', 'CX-5', 1, 64.0))

for i in range(4):
    dealer.available_cars.append(Electric('blue', 'Tesla', 'Model S', 1, 79.0))

for i in range(8):
    dealer.available_cars.append(Petrol('red', 'Toyota', 'Prius', 1, 45.0))

Dealer.available_cars[34].print_make_and_model()

# Check the correct number of cars were added to the list.
count = 0
for car in Dealer.available_cars:
    count += 1

print count

def main():  
    root = tk.Tk()
    root.title("Angier Car Rental")
    root.geometry("500x600")
    app = CarRentalView(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  