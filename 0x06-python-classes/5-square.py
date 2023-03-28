#!/usr/bin/python3
"""Python Classes and Objects."""

class Square:
    """Creates an empty class Square which defines a square."""
    
    def __init__(self, size=0):
        """The init method instantiates the empty class
        with a new object.
        Args:
            size = size of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if the value of size is negative.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of the square.
        Prints result.
        """

        ar = self.__size ** 2
        return ar
 
    @property
    def size(self):
        """Gets value of size object."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets value of size object."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
       """If value of size is positive, method prints
       a square."""

       if self.__size < 0:
           print()
       else:
           for i in range(self.__size):
               for j in range(self.__size):
                   print("#", end="")
               print()
