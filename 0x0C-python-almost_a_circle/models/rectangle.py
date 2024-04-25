#!/usr/bin/python3
"""
Module defines class inheriting from Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Creates new subclass.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor call initializes class with private instance
        attributes and public superclass attribute.
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter method retrieves value of width. """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method sets new width value.

        Args:
            value: new value of width

        Raises:
            TypeError: width must be integer.
            ValueError: width must be positive non-zero.
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ Getter method retrieves value of height. """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method sets new height value.

        Args:
            value: new value of height

        Raises:
            TypeError: height must be integer.
            ValueError: height must be positive non-zero.
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ Getter method retrieves value of x. """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method sets new x value.

        Args:
            value: new value of x-coordinate.

        Raises:
            TypeError: x-coordinate must be integer.
            ValueError: x-coordinate must be positive.
        """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ Getter method retrieves y of width. """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method sets new y value.

        Args:
            value: new value of y-coordinate.

        Raises:
            TypeError: y-coordinate must be integer.
            ValueError: y-coordinate must be positive.
        """

        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def __str__(self):
        """
        Returns string representation of instance id,
        x and y coordinates, rectangle width and height.
        """
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} -' \
               f' {self.width}/{self.height}'

    def area(self):
        """
        Instance method returns area of rectangle.

        Args:
            width: width of rectangle.
            height: height of rectangle.

        Returns:
            Area of rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Instance method prints rectangle to console
        along x and y-coordinates.
        """

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """
        Instance method updates attribute values.

        Args:
            *args: new instance attribute values.
            **kwargs: dictionary of attribute name
            and corresponding values.

        Returns:
            Updated attribute values.
        """

        attr = ('id', 'width', 'height', 'x', 'y')
        for idx in range(len(args)):
            setattr(self, attr[idx], args[idx])
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Instance method returns dictionary containing
        attribute-value pair of class Rectangle.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
