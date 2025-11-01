#!/usr/bin/python3

#!/usr/bin/python3
"""Defines a Square class with size, position, area, and print behavior."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with optional size and position."""
        self.size = size          # uses the setter for validation
        self.position = position  # uses the setter for validation

    # -------- size property --------
    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # -------- position property --------
    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation (tuple of 2 positive integers)."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # -------- area --------
    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    # -------- my_print --------
    def my_print(self):
        """Print the square with '#' using its position.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print("")

        # print each row with horizontal offset then hashes
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

