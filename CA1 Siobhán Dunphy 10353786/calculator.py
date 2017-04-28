# Siobhan Dunphy
# Student number: 10353786

# create a class called calculator that can add, subtract, divide, multiply, exponent, 
from math import *
from tkinter import *

# Create object as the calculator interface
# Create text display for the calculator
# Create the window name
frame  = Tk()
display = Entry(frame, width = 12, justify = 'right',bd = 0, bg = 'hot pink')
frame.title("Calculator")

# Create the calculator class
class Calculator:
    # init method for anytime you create a calculator object. Creates variables and specifies the initial values.
    def __init__(self):
        self.var1 = " "
        self.var2 = " "
        self.result = 0
        self.current = 0
        self.operator = 0
        
    # Append the input numbers by clearing the current display and displaying the appended variables.
    def num_button(self, input):
        if self.current is 0:
            self.var1 = str(self.var1) + str(input)
            display.delete(0,END)
            display.insert(0,string = self.var1)
        else:
            self.var2 = str(self.var2) + str(input)
            display.delete(0,END) 
            display.insert(0,string = self.var2)
    
    ####### A function is also required to take in negative numbers in the GUI but is not yet written!
    # def sign(self, input):      
    # Define methods for each mathematical operation.
    # 1. Add
    # 2. Subtract
    # 3. Multiply
    # 4. Divide
    # 5. Exponent
    # 6. Square
    # 7. Sin
    # 8. Cos
    # 9. Tan
    # 10. Log to base 10 
    def add(self, x, y):
        x = float(x)
        y = float(y)
        return x + y
    
    def subtract(self, x, y):
        x = float(x)
        y = float(y)
        return x - y
    
    def multiply(self, x, y):
        x = float(x)
        y = float(y)
        return x * y
    
    def divide(self, x, y):       
        x = float(x)
        y = float(y)
        if y == 0:
            return 'NaN'
        return x / float(y)

    def power(self, x, y):
        x = float(x)
        y = float(y)
        if y == 0:
            return 1
        return x**y
    
    def square(self, x):
        x = float(x)
        return x*x
    
    def sin_func(self,x):
        x = float(x)
        return sin(x)
        
    def cos_func(self,x):
        x = float(x)
        return cos(x)
    
    def tan_func(self,x):
        x = float(x)
        return tan(x)  
    
    def logarithm(self,x):
        x = float(x)
        if x <= 0:
            return 'NaN'
        return log(x,10)
    
    def set_op(self,op):
        self.operator = op
        display.delete(0,END)
        if self.current is 0:
            self.current = 1
        else:
            self.equate()
            self.var2 = " "
            
    def equate(self):
        if self.operator is 0:
            self.result = self.add(self.var1, self.var2)
        elif self.operator is 1:
            self.result = self.subtract(self.var1, self.var2)
        elif self.operator is 2:
            self.result = self.multiply(self.var1, self.var2)
        elif self.operator is 3:
            self.result = self.divide(self.var1, self.var2)
        elif self.operator is 4:
            self.result = self.power(self.var2)
        elif self.operator is 5:
            self.result = self.square(self.var1)   
        elif self.operator is 6:
            self.result = self.sin_func(self.var2)   
        elif self.operator is 7:
            self.result = self.cos_func(self.var2)   
        elif self.operator is 8:
            self.result = self.tan_func(self.var2)   
        elif self.operator is 9:
            self.result = self.logarithm(self.var2)      
        display.delete(0,END)
        display.insert(0,string=self.result)
    
    # method to reset the calculator
    def clear(self):
        self.__init__() # calls the function __init__ within the class
        display.delete(0,END)
          
# Create a calculator object
calc = Calculator() 

# Create the buttons
b0 = Button(frame, text = "0", command = lambda: calc.num_button(0))
b1 = Button(frame, text = "1", command = lambda: calc.num_button(1))
b2 = Button(frame, text = "2", command = lambda: calc.num_button(2))
b3 = Button(frame, text = "3", command = lambda: calc.num_button(3))
b4 = Button(frame, text = "4", command = lambda: calc.num_button(4))
b5 = Button(frame, text = "5", command = lambda: calc.num_button(5))
b6 = Button(frame, text = "6", command = lambda: calc.num_button(6))
b7 = Button(frame, text = "7", command = lambda: calc.num_button(7))
b8 = Button(frame, text = "8", command = lambda: calc.num_button(8))
b9 = Button(frame, text = "9", command = lambda: calc.num_button(9))
b_decimal = Button(frame, text = ".", command = lambda: calc.num_button("."))

plus = Button(frame, text = "+", command = lambda: calc.set_op(0))
minus = Button(frame, text = "-", command = lambda: calc.set_op(1))
times = Button(frame, text = "*", command = lambda: calc.set_op(2))
div = Button(frame, text = "/", command = lambda: calc.set_op(3))
pow = Button(frame, text = "^", command = lambda: calc.set_op(4))
square = Button(frame, text = "x^2", command = lambda: calc.set_op(5))
sine = Button(frame, text = "sin", command = lambda: calc.set_op(6))
cosine = Button(frame, text = "cos", command = lambda: calc.set_op(7))
tangent = Button(frame, text = "tan", command = lambda: calc.set_op(8))
log10 = Button(frame, text = "log", command = lambda: calc.set_op(9))

equals = Button(frame, text = "=", command = calc.equate) # lambda not required since no parameters
clear = Button(frame, text = "c", command = calc.clear)

# Position buttons on the screen
display.place(x=0,y=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b0.grid(row=4, column=0)

b_decimal.grid(row=4, column=1)
clear.grid(row=5, column=3)
equals.grid(row=5, column=4)
#plusminus.grid(row=4, column=2)

plus.grid(row=0, column=3)
minus.grid(row=1, column=3)
times.grid(row=2, column=3)
div.grid(row=3, column=3)
pow.grid(row=4, column=3)
square.grid(row=0, column=4)
sine.grid(row=1, column=4)
cosine.grid(row=2, column=4)
tangent.grid(row=3, column=4)
log10.grid(row=4, column=4)

frame.mainloop()      

