# CA5 part B - involves modifying your calculator class from CA1 to ensure that it can handle lists of data.
# You will be required to refactor / rewrite your functions so that they can handle lists.
# You will need to use lambda, map, filter, reduce and list comprehension in any manner you deem necessary to achieve this.

# class CalculatorList(object):
#     def __init__(self):
#         self.numbers=[]
# 
#     def add(self, x, y):
#         x = float(x)
#         y = float(y)
#         return x + y
import math

print "Wecome to the list calculator!"
nums = []
list = []
result = []
ops = ('+', '-', '/', '*', 'power', 'square', 'sin','cos', 'tan', 'log')

# Create recursive function to get list of numbers.
def get_list():
    str_inp = raw_input("Please enter any number, '=' to calculate the result, or Q to quit:\n")
    if str_inp == '=':
        return nums
    else:
        num = float(str_inp)        
        nums.append(num)
        get_list()

# Create a function to call the correct operation depending on the input.
def command(operator, list):
    if operator == '+':
        result = reduce(lambda x,y: x+y, list)
    elif operator == '-':
        result = reduce(lambda x,y: x-y, list)
    elif operator == '/':
        result = reduce(lambda x,y: x/y, list)
    elif operator == '*':
        result = reduce(lambda x,y: x*y, list)
    elif operator == 'power':
        result = map(lambda x,y: x**y, list)
    return result

# Create some functions to perform the mathematical operations.
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

while True:   
    inp = raw_input("Please enter the operation you would like to perform on a list: +, -, /, *, power, square, sin, cos, tan, or log, or type Q to quit!\n")
    if inp.lower() == 'q':
        print "Thank you for using the list calculator."
        break
    elif inp in ops:
        op = inp
        get_list()
        result = command(op, nums)
        print result
