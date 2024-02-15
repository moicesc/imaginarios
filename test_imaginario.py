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
    x = 1.0 + 1.0j
    y = 2.0 + 4.0j
    return a, b, x, y


def test_addition(test_numbers):
    """Test addition operation"""
    a, b, x, y = test_numbers
    result_addition = a + b
    expected_result = x + y
    assert result_addition.real == expected_result.real
    assert result_addition.imag == expected_result.imag


def test_subtraction(test_numbers):
    """Test subtraction operation"""
    a, b, x, y = test_numbers
    result_subtraction = a - b
    expected_result = x - y
    assert result_subtraction.real == expected_result.real
    assert result_subtraction.imag == expected_result.imag


def test_multiplication(test_numbers):
    """Test multiplication operation"""
    a, b, x, y = test_numbers
    result_multiplication = a * b
    expected_result = x * y
    assert result_multiplication.real == expected_result.real
    assert result_multiplication.imag == expected_result.imag


def test_division(test_numbers):
    """Test division operation."""
    a, b, x, y = test_numbers
    result_division = a / b
    expected_result = x / y
    assert result_division.real == pytest.approx(expected_result.real, rel=1e-6, abs=1e-12)
    assert result_division.imag == pytest.approx(expected_result.imag, rel=1e-6, abs=1e-12)
