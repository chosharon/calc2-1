"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):

    def getResult(self):
        return self.value_a + self.value_b