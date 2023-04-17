#!/usr/bin/python3
"""Method presents Rectangle methods."""
from models.base import Base


class Rectangle(Base):
    """Creates inherited class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class instantiates inherited class."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Method retrieves width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method sets value of width."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Method retrieves height value"""
        return self.__height

    @property
    def height(self):
        """Method retrieves height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method sets value of height."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Method retrieves x's value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method sets value of x."""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Method retrieves width value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method sets value of y."""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Computes and returns area of rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle to stdout."""
        for new_line in range(self.y):
            print("")
        for rows in range(self.__height):
            for indent in range(self.x):
                print(" ", end="")
            for columns in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Method returns printed output."""
        return "[Rectangle] ({:d}) {:d}/{:d} - " \
               "{:d}/{:d}".format(self.id, self.x, self.y,
                                  self.width, self.height)

    def update(self, *args, **kwargs):
        """Method assigns arguments."""
        length = len(args)

        if args is not None and length != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for l in range(length):
                setattr(self, attributes[l], args[l])
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Method returns dictionary representation of Rectangle"""
        return {'id': self.id, 'width': self.__width, 'height':
            self.__height, 'x': self.__x, 'y': self.__y}
