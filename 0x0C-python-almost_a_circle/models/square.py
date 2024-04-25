#!/usr/bin/python3
"""
Module creates class inheriting from
Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Creates new subclass.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor call initializes class with
        inherited private attributes.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints string representation of square id,
        dimension, and x-y coordinates to console.
        """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """
        Getter method retrieves value of Rectangle
        width for Square dimension.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method assigns new value to width
        and height of rectangle.

        Args:
            value: new value for width and height.
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Instance method updates square instance
        attribute values.
        """

        attr = ('id', 'size', 'x', 'y')
        for idx in range(len(args)):
            setattr(self, attr[idx], args[idx])

        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Instance method returns a dictionary of
        attribute-value parie for Square class.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
