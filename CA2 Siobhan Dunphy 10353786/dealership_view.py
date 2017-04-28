from Tkinter import *
import Tkinter as tk

from dealership import Dealership
from car import Car, Petrol, Diesel, Electric, Hybrid

# Create class for GUI of dealership
class CarRentalView(tk.Frame):
    def __init__(self, master, name):
        tk.Frame.__init__(self, master)    
        self.master=master
        self.message = ""
        self.booking_ref = ""
        self.entries = []
        self.fields = 'Firstname', 'Lastname', 'Address', 'Phone', 'Email'
        
        # Create an instance of a dealership
        self.dealer = Dealership(name)
        
        # Add some cars to the dealership instance.
        self.add_cars()
        
        # Call the function to create the user interface.
        self.initUI()
    
    # Function to initialise the user interface and create display and input fields.
    def initUI(self):
        output_frame = tk.Frame(self, relief='raised', borderwidth=1)
        welcome_message = tk.Label(output_frame, text="Hello! Welcome to Angier Car Rental!")
        output_text = tk.Text(output_frame, height=4, width=80)
        output_frame.pack(fill='both',expand=True)
        welcome_message.pack(padx=5, pady=5)
        output_text.pack(side='left', fill='y', padx=5, pady=5)
        
        output_text.config(font=('Arial', 14, 'italic'))
        welcome_message.config(font=('Arial', 16, 'bold', 'italic'))
        
        self.message = "To check availability, please enter your requirements and select Booking Enquiry.\n\nTo make a booking, please enter your details and select Booking Request.\n\nTo return a car(s), please enter your booking ID and select Return Car."
        output_text.insert('end', self.message)
        
        # Set up the drop down menus
        options_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = "Please select your requirements: ")
        options_frame.pack(fill='both',expand=True)
        
        self.car_var = tk.StringVar()
        self.num_var = tk.StringVar()
        
        car_type = {'Petrol','Diesel','Electric','Hybrid'}
        self.car_var.set('Petrol') # default option
        car_type_drop = tk.OptionMenu(options_frame, self.car_var, *car_type)
        car_type_drop.pack(side="left")
        
        number_cars = {'1 car','2 cars','3 cars','4 cars'}
        self.num_var.set('1 car') # default option    
        number_cars_drop = tk.OptionMenu(options_frame, self.num_var, *number_cars)
        number_cars_drop.pack(side="left")
        
        days = tk.Label(options_frame, text="Number of days")
        self.input_days = tk.Entry(options_frame)
        self.input_days.pack(side='left')
        self.input_days.pack(side='left')
        
        # Create a message frame
        self.message_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = "Message:")
        self.message_frame.pack(fill='both',expand=True)
        self.message_text = tk.Text(self.message_frame, height=4, width=80)
        self.message_text.pack(side='left', fill='y', padx=5, pady=5)
        self.message_text.config(font=('Arial', 14, 'bold', 'italic'))
        self.message_text.insert('end', "")
        
        # Set up the command buttons
        command_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = "Please select an option: ")
        command_frame.pack(side='bottom',fill='both',expand=True)
        
        enquiry_button = tk.Button(command_frame, text = "Booking Enquiry", bg="blue", command = lambda: self.booking_enquiry_button()) 
        enquiry_button.pack(side='left', padx=5, pady=5)
        
        booking_button = tk.Button(command_frame, text = "Booking Request", bg="blue", command = lambda: self.booking_request_button()) 
        booking_button.pack(side='left', padx=5, pady=5)
        
        returns_button = tk.Button(command_frame, text = "Return Car", bg="blue", command = lambda: self.return_a_car_button())
        returns_button.pack(side='left', padx=5, pady=5)
        
        #quit_button = tk.Button(command_frame, text="Quit", bg="blue")
        #quit_button.pack(side='left', padx=5, pady=5)
        
        # Set up the customer details
        self.create_customer_form(self.fields)
        
        # Set up the return frame
        return_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = "For returns only: ")
        return_frame.pack(fill='both',expand=True)
        lab_id = tk.Label(return_frame, text = "Booking reference")
        lab_id.pack(side='left', padx=5, pady=5)
        self.booking_id = tk.Entry(return_frame)
        self.booking_id.pack(side='left', padx=5, pady=5)
        
        self.pack(fill='both', expand=True)
    
    # Function to create customer input form.
    def create_customer_form(self, fields):       
        customer_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = 'Please enter your details (for booking requests only): ')
        customer_frame.pack(fill='both',expand=True)
        for field in fields:
            row = tk.Frame(customer_frame)
            lab = tk.Label(row, text=field, anchor='w')
            ent = tk.Entry(row)           
            row.pack(side='top', padx=5, pady=5)
            lab.pack(side='left')
            ent.pack(side='right')
            self.entries.append((field, ent))
        return
    
    # Function to create a booking reference for customer.
    def generate_booking_ref(self):
        x=['Lastname']
        y=['Phone']
        ref_name = self.dealer.customer[x[0]]
        ref_num = self.dealer.customer[y[0]]
        length = len(ref_num)
        self.booking_ref = ref_name + ref_num[length-4:length] 
        return self.booking_ref
    
    # Function takes values from the input form, creates a new customer dict, generates a booking ref, and adds the customer dict 
    # to a list of customers. Returns 0 if no customer is created and booking_ref if a customer has been created.
    def new_customer(self):
        for entry in self.entries:
            field = entry[0]
            val  = entry[1].get()
            # Check if input exist and if not reset customer dict to empty.
            if len(val) == 0:
                return 0
            else:
                self.dealer.customer.update({field:val})
        booking_ref = self.generate_booking_ref()
        self.dealer.customer.update({"BookingRef":booking_ref})
        self.dealer.customer.update({"NumberOfCars": self.num_var.get()})
        self.dealer.customer.update({"TypeOfCar": self.car_var.get()})
        self.dealer.customers.append(self.dealer.customer)
        print('New customer created.')
        return self.booking_ref
    
    # Function to display a message on screen for the customer.    
    def output_message(self, message):
        self.message_text.delete(1.0,END)
        #self.message_text = tk.Text(self.message_frame, height=4, width=80)
        self.message_text.pack(side='left', fill='y', padx=5, pady=5)
        self.message_text.config(font=('Arial', 14, 'bold', 'italic'))
        self.message_text.insert('end', message)
        return
    
    # Function that checks if cars available.  
    def booking_enquiry_button(self):
        car_type = self.car_var.get()
        num_cars = self.num_var.get()
        num_cars_int = num_cars[0]
        num_cars_int = int(num_cars_int)
        # Check availability by calling function in dealereship
        number = self.dealer.check_availability(car_type)
        if number>=num_cars_int:
            self.message = "You're in luck! We have %s %s cars available.\n" %(num_cars_int, car_type)
        else:
            self.message = "Sorry, only %s %s cars available.\n" %(number, car_type)
        self.output_message(self.message)

    # Function to make booking 
    def booking_request_button(self):        
        car_type = self.car_var.get()
        num_cars = self.num_var.get()
        num_cars_int = num_cars[0]
        num_cars_int = int(num_cars_int)
        days = self.input_days.get()
        # Update total cars available and print values for available cars and total profit.
        self.dealer.customer = self.new_customer() 
        if self.dealer.customer ==0:
            self.message = "Please fill in all relevant fields.\n"
            self.output_message(self.message)
        else:
            self.message = self.dealer.car_rental(car_type, num_cars_int, days)
            self.ref = "Your booking reference: %s\n" %self.booking_ref 
            self.output_message(self.message+self.ref)
            # Report total remaining cars and total profits to terminal
            self.dealer.total_available = self.dealer.check_total_cars_available()
            print "Total remaining cars available: %s\n" %self.dealer.total_available
            print "Total profits: %s\n" %self.dealer.profit
    
    # Function to return car.     
    def return_a_car_button(self):
        booking_ref = self.booking_id.get()
        # Access the list of customers to check if booking ref exists and remove customer
        i=0
        try:
            for customer in self.dealer.customers:
                if customer['BookingRef'] == booking_ref:
                    car_type = customer['TypeOfCar']
                    num_cars = customer['NumberOfCars']
                    self.dealer.customers.remove(customer)
                    self.message = self.dealer.car_return(car_type, num_cars)
                    break
        except:
            self.message = "Sorry, no record of booking.\n"
            self.output_message(self.message)
        self.output_message(self.message)
        self.dealer.total_available = self.dealer.check_total_cars_available()
        print "Total remaining cars available: %s\n" %self.dealer.total_available
        return
    
    def add_cars(self):
    # Add cars to the available_cars list in the newly created dealership instance
        for i in range(20):
            self.dealer.available_cars.append(Petrol('green', 'VW', 'Golf', 56.0))
    
        for i in range(8):
            self.dealer.available_cars.append(Diesel('silver', 'Mazda', 'CX-5', 64.0))

        for i in range(4):
            self.dealer.available_cars.append(Electric('blue', 'Tesla', 'Model S', 79.0))

        for i in range(8):
            self.dealer.available_cars.append(Hybrid('red', 'Toyota', 'Prius', 45.0))

def main():  
    root = tk.Tk()
    root.title("Angier Car Rental")
    root.geometry("600x600")
    app = CarRentalView(root, 'Aungier Car Rental')
    root.mainloop()  

if __name__ == '__main__':
    main()  