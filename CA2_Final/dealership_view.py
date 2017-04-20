from Tkinter import *
import Tkinter as tk

from dealership import Dealership
from car import Car, Petrol, Diesel, Electric, Hybrid

# Create class for graphical user interface of dealership
class CarRentalView(tk.Frame):
    def __init__(self, master, name):
        tk.Frame.__init__(self, master)    
        self.master=master
        self.message = ""
        self.booking_ref = ""
        self.dealer = Dealership(name)
        self.add_cars()
        self.customers = {}
        self.entries = []
        self.fields = 'Firstname', 'Lastname', 'Address', 'Phone', 'Email'
        self.message_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = "Message:")
        self.message_frame.pack(fill='both',expand=True)
        self.initUI()
        
    def customer_form(self, fields):       
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
    
    def generate_booking_ref(self):
        x=['Lastname']
        y=['Phone']
        ref_name = self.customers[x[0]]
        ref_num = self.customers[y[0]]
        length = len(ref_num)
        self.booking_ref = ref_name + ref_num[length-4:length] 
        return self.booking_ref
    
    def new_customer(self):
        for entry in self.entries:
            field = entry[0]
            val  = entry[1].get()
            self.customers.update({field:val})
        booking_ref = self.generate_booking_ref()
        self.customers.update({"Booking ref":booking_ref})
        print('New customer created.')
        print(self.booking_ref)
        return self.booking_ref
        
    def output_message(self, message):
        self.message = message
        if self.message_frame.winfo_exists() == 0:  
            self.message_frame.pack_forget()
        self.message_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = "Message:")
        self.message_frame.pack(fill='both',expand=True)
        message_text = tk.Text(message_frame, height=4, width=80)
        message_text.pack(side='left', fill='y', padx=5, pady=5)
        message_text.config(font=('Arial', 14, 'bold', 'italic'))
        message_text.insert('end', self.message)
        return
    
    def get_car_type(self,value):
        return value
   
    def get_num_cars(self,value):
        return value
    
    def booking_enquiry_button(self):
        pass

    def booking_request_button(self):
        customer = self.new_customer()
        
        car_type = self.car_var.get()
        num_cars = self.num_var.get()
        num_cars_int = num_cars[0]
        num_cars_int = int(num_cars_int)
        days = self.input_days.get()
        days = int(days)
        self.message = self.dealer.car_rental(car_type, num_cars_int, days)
        
        #self.message ="Congratulations! You have successfully made a booking!\n\nYou're booking ref: %s" %self.booking_ref
        #print("Congratulations! You have successfully made a booking! You're booking ref is: %s" %self.booking_ref)
        self.output_message(self.message)
        return
            
    def return_a_car_button(self):
            pass
    
    def add_cars(self):
    # Add cars to the available_cars list in the newly created dealership instance
        for i in range(20):
            self.dealer.available_cars.append(Petrol('green', 'VW', 'Golf', 56.0))
    
        for i in range(8):
            self.dealer.available_cars.append(Diesel('silver', 'Mazda', 'CX-5', 64.0))

        for i in range(4):
            self.dealer.available_cars.append(Electric('blue', 'Tesla', 'Model S', 79.0))

        for i in range(8):
            self.dealer.available_cars.append(Petrol('red', 'Toyota', 'Prius', 45.0))
    
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
        
        # Set up the command buttons
        command_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = "Please select an option: ")
        command_frame.pack(side='bottom',fill='both',expand=True)
        
        enquiry_button = tk.Button(command_frame, text = "Booking Enquiry", bg="blue") 
        enquiry_button.pack(side='left', padx=5, pady=5)
        
        booking_button = tk.Button(command_frame, text = "Booking Request", bg="blue", command = lambda: self.booking_request_button()) 
        booking_button.pack(side='left', padx=5, pady=5)
        
        returns_button = tk.Button(command_frame, text = "Return Car", bg="blue")
        returns_button.pack(side='left', padx=5, pady=5)
        
        quit_button = tk.Button(command_frame, text="Quit", bg="blue")
        quit_button.pack(side='left', padx=5, pady=5)
        
        # Set up the customer details
        self.customer_form(self.fields)
        
        # Set up the return frame
        return_frame = tk.LabelFrame(self, relief='raised', borderwidth=1, text = "For returns only: ")
        return_frame.pack(fill='both',expand=True)
        lab_id = tk.Label(return_frame, text = "Booking number")
        lab_id.pack(side='left', padx=5, pady=5)
        booking_id = tk.Entry(return_frame)
        booking_id.pack(side='left', padx=5, pady=5)
        
        self.pack(fill='both', expand=True)
    
        #def output(self):
         #   print "Sorry, no cars available. Please try again later or modify your choices."
        # print "You're in luck! Total price = "
           # print "Congratualations your booking is complete!"
            #print "You have successfully returned your car. Thank you for booking with us!"

def main():  
    root = tk.Tk()
    root.title("Angier Car Rental")
    root.geometry("600x600")
    app = CarRentalView(root, 'Aungier Car Rental')
    root.mainloop()  

if __name__ == '__main__':
    main()  