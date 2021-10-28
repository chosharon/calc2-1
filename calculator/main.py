""" This is the increment function"""

def inc(x_value):
    """ Increment Function adds one to the x_value"""
    return x_value + 1

class Calculator:
    """ This is the Calculator class"""

    result = 0
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtracts number from result"""
        self.result = self.result - value_a
        return self.result

    def multiply_numbers(self, value_a, value_b):
        """ multiplies number with result """
        self.result = value_a * value_b
        return self.result
    def divide_numbers(self, value_a, value_b):
        """ divides number by result """
        if value_a == 0:
            print (0)
        elif value_b == 0:
            print ("error")
        else:
            self.result = value_a / value_b

        return self.result
