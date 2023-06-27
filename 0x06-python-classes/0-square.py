#!/usr/bin/python3
"""defines class square """

    class Square:
    """An empty class that represents a square.

    Attributes:
        side: The length of the side of the square.
    """

    def __init__(self, side: float) -> None:
        """Initializes a square with a given side length.

        Args:
            side: The length of the side of the square.
        """
        self.side = side
