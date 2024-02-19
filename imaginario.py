# python3
"""
Essential implementation for imaginary numbers.
"""
import math
from typing import Tuple


class Imaginario:
    """A class to represent complex numbers."""

    def __init__(self, real: float, imag: float):
        """Initialize a complex number.

        Args:
            real (float): The real part of the complex number.
            imag (float): The imaginary part of the complex number.

        """
        self.real = real
        self.imag = imag

    def __repr__(self) -> str:
        """Return a string representation of the complex number."""
        return f"{self.real} + {self.imag}j"

    def __add__(self, other: 'Imaginario') -> 'Imaginario':
        """Add two complex numbers.

        Args:
            other (Imaginario): The complex number to be added

        Returns:
            Imaginario: The result of the addition.
        """
        return Imaginario(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: 'Imaginario') -> 'Imaginario':
        """Subtract two complex numbers.

        Args:
            other (Imaginario): The complex number to be subtracted

        Returns:
            Imaginario: The result of the subtraction.
        """
        return Imaginario(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other: 'Imaginario') -> 'Imaginario':
        """Multiply two complex numbers.

        Args:
            other (Imaginario): The complex number to be multiplied.

        Returns:
            Imaginario: The result of the multiplication.
        """
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real

        return Imaginario(real_part, imag_part)

    def __truediv__(self, other: 'Imaginario') -> 'Imaginario':
        """Divide two complex numbers.

        Args:
            other (Imaginario): The complex denominator

        Returns:
            Imaginario: The result of the division.
        """
        denominator = other.real ** 2 + other.imag ** 2

        if denominator == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator

        return Imaginario(real_part, imag_part)

    # TODO: Implement absolute value method
    def __abs__(self):
        pass

    # TODO: Implement power method
    def __pow__(self, power, modulo=None):
        pass

    @property
    def magnitude(self) -> float:
        """Calculate the magnitude of a complex number.

        Returns:
            The magnitude of the complex number.
        """
        return math.sqrt(self.real**2 + self.imag**2)

    @property
    def phase(self) -> float:
        """Calculate the phase of a complex number.

        Returns:
            The phase of the complex number in polar form.
        """
        return math.atan2(self.imag, self.real)

    @classmethod
    def from_polar(cls, magnitude: float, phase: float) -> 'Imaginario':
        """Class method to provide an alternative constructor from the polar form.

        Args:
            magnitude (float): magnitude of the complex number.
            phase (float): phase of the complex number

        Returns:
            Imaginario: Complex number
        """
        real_part = magnitude * math.cos(phase)
        imag_part = magnitude * math.sin(phase)
        return cls(real_part, imag_part)

    def to_polar(self) -> Tuple[float, float]:
        """Converts the complex number to polar form.

        Returns:
            Tuple with the magnitude and the phase of the complex number.
        """
        magnitude = self.magnitude
        phase = self.phase
        return magnitude, phase
