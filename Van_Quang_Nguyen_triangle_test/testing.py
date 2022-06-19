import pytest

from calculation import Result



"""
the assert function is checking if the statement is true.
it is used when debugging code
and test if a condition in your code returns True, if not, the program will raise an AssertionError

"""

def test_two():
    test_cls = Result("data_testing.csv")

    test_data = [{'Comp': [0, 0, 0, 0, 0, 0, 0, 110.0, 280.0, 200.0],
                  'Non-Comp': [45.2, 110.0, 110.0, 147.0, 50.0, 125.0, 150.0, 55.0, 140.0, 100.0]}]

    assert test_cls.fin_results == test_data

