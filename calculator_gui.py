# use Python's built-in library tkinter to build GUI
from tkinter import *
from math import *

# Create object as the calculator interface
# Create text display for the calculator
# Create the window name
frame  = Tk()
display = Entry(frame, width=12, justify='right',bd=0, bg='hot pink')
frame.title("Calculator")
            
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
exp = Button(frame, text = "^", command = lambda: calc.set_op(4))

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
clear.grid(row=4, column=2)
equals.grid(row=4, column=3)
plus.grid(row=0, column=3)
minus.grid(row=1, column=3)
times.grid(row=2, column=3)
div.grid(row=3, column=3)
exp.grid(row=4, column=3)

frame.mainloop()      