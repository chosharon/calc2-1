from calc.calculations.division import Division

def test_calculator_divide_static():
    division = Division(4, 2)
    assert division.get_result() == 2