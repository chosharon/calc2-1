from calc.calculations.calculation import Calculation

class Division(Calculation):
    def get_result(self):
        result = self.values[0]
        for val in self.values[1:]:
            result /= val
        return result