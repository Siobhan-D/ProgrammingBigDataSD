# use Python's built-in library tkinter to build GUI
from tkinter import *

# Create frame object as the calculator
# Create text display for the calculator
# Create the window name
frame  = Tk()
display = Entry(frame, width=12, justify='right',bd=0, bg='Brightpink')
frame.title("Calculator")

# Create the calculator class
class Calculator:
    # init method for anytime you create a calculator object. Creates variables and pecifies the initial values.
    def __init__(self):
        self.var1= " "
        self.var2= " "
        self.result=0
        self.current=0
        self.operator=0
        
    def num_but(self, input):
        if self.current==0:
            self.var1=str(self.var1)+str(input)
            display.delete(0,END)
            display.insert(0,string=self.var1)
        else:
            self.var2=str(self.var2)+str(input)
            display.delete(0,END)
            display.insert(0,string=self.var2)
    
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):       
        if y == 0:
            return 'NaN'
        return x / float(y)

    def exponent(self, x, y):
        return x ** y
    
    def equate(self):
        var1 = float(var1)
        var2 = float(var2)
        if self.operator == 0:
            self.result = self.add(var1, var2)
        elif self.operator ==1:
            self.result = self.subtract(var1, var2)
        elif self.operator ==2:
            self.result = self.multiply(var1, var2)
        elif self.operator ==3:
            self.result = self.divide(var1, var2)
        elif self.operator ==4:
            self.result = self.exponent(var1, var2)
            
            
            