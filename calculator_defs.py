class Calculator(object):

    number_types = (int, long, float, complex)
    
    def add(self, x, y):
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def divide(self, x, y):
        
        if y == 0:
            return 'NaN'
        return x / float(y)

    def exponent(self, x, y):
        return x ** y

    def multiply(self, x, y):
        return x * y

    def subtract(self, x, y):
        return x - y
        
