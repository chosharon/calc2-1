""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

class Calculator:
	"""this is the calculator class"""
	history = []    #this is global

	@staticmethod
	def add_numbers(value_a, value_b):
		"""adds two numbers"""
		addition = Addition(value_a, value_b)
		Calculator.history.append(addition)
		return addition.getResult()

	@staticmethod
	def subtract_numbers(value_a, value_b):
		"""subtract numbers from result"""
		subtraction = Subtraction(value_a, value_b)
		Calculator.history.append(subtraction)
		return subtraction.get_result()

	@staticmethod
	def multiply_numbers (value_a, value_b):
		multiplication = Multiplication(value_a, value_b)
		Calculator.history.append(multiplication)
		return multiplication.get_result()

	@staticmethod
	def divide_numbers(value_a, value_b):
		division = Division(value_a, value_b)
		Calculator.history.append(division)
		return division.get_result()

	@staticmethod
	def history_length():
		return len(Calculator.history)

	@staticmethod
	def get_first_history_obj():
		return Calculator.history[0]

	@staticmethod
	def get_first_history_result():
		obj = Calculator.get_first_history_obj()
		return obj.get_result()

	@staticmethod
	def get_last_history_obj():
		index = Calculator.history_length() - 1
		return Calculator.history[index]

	@staticmethod
	def get_last_history_result():
		obj = Calculator.get_last_history_obj()
		return obj.get_result()


	@staticmethod
	def history_remove(index):
		Calculator.history.pop(index)

	@staticmethod
	def clear_history():
		Calculator.history = []


'''
def inc(x_value):
	""" Increment Function adds one to the x_value"""
	return x_value + 1

class Calculator:
	""" This is the Calculator class"""

	result = 0
	def get_result(self):
		""" Get Result of Calculation"""
		return self.result

	def add_numbers(self, value_a):
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

		return self.result'''

