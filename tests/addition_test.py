""" content of calculator.py#"""
from calc.calculations.addition import Addition

def test_calculation_addition():

    #Arrange
    addition = Addition(1, 2)
    #Act
    result = addition.getResult()
    #Assert
    assert result == 3
