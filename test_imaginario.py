"""
Tests for Imaginario functionality
"""
import pytest

from imaginario import Imaginario


@pytest.fixture
def test_numbers():
    """Test values for the arithmetic of complex numbers."""
    a = Imaginario(1.0, 1.0)
    b = Imaginario(2.0, 4.0)
    return a, b


def test_addition(test_values):
    """Test addition operation"""
    a, b = test_values
    result_addition = a + b
    assert result_addition.real == 3.0
    assert result_addition.imag == 5.0


def test_subtraction(test_values):
    """Test subtraction operatio"""
    a, b = test_values
    result_subtraction = a - b
    assert result_subtraction.real == -1.0
    assert result_subtraction.imag == -3.0
