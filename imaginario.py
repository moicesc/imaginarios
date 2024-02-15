# python3
"""
Essential implementation for imaginary numbers.
"""


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
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Imaginario(real_part, imag_part)
