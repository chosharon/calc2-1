from calc.calculations.multiplication import Multiplication

def test_calculator_multiply_static():
    multiplication = Multiplication(2, 2)
    assert multiplication.get_result() == 4