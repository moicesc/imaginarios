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
