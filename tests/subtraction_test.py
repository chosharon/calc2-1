from calc.calculations.subtraction import Subtraction

def test_calculator_subtract_static():
    subtraction = Subtraction(6, 2)
    assert subtraction.get_result() == 4