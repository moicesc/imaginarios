import pytest

from imaginario import Imaginario


@pytest.fixture
def test_numbers():
    a = Imaginario(1.0, 1.0)
    b = Imaginario(2.0, 4.0)
    return a, b


def test_addition(test_numbers):
    a, b = test_numbers
    result_addition = a + b
    assert result_addition.real == 3.0
    assert result_addition.imag == 5.0


def test_subtraction(test_numbers):
    a, b = test_numbers
    result_subtraction = a - b
    assert result_subtraction.real == -1.0
    assert result_subtraction.imag == -3.0
