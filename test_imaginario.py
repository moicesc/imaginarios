import pytest

from imaginario import Imaginario


def test_addition():
    a = Imaginario(1.0, 1.0)
    b = Imaginario(2.0, 2.0)
    result = a + b
    assert result.real == 3.0
    assert result.imag == 3.0
