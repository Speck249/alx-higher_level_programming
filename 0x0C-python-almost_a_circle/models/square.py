#!/usr/bin/python3
"""Method presents square methods."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates inherited class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Method instantiates inherited class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method returns string representation"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Method retrieves size."""
        return self.width

    @size.setter
    def size(self, value):
        """Method sets value of size."""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method assigns arguments."""

        length = len(args)

        if args is not None and length != 0:
            attributes = ['id', 'size', 'x', 'y']
            for k in range(length):
                if args[k] == 'size':
                    setattr(self, 'width', args[k])
                    setattr(self, 'height', args[k])
                else:
                    setattr(self, attributes[k], args[k])
        else:
            for name, value in kwargs.items():
                if name == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Method returns dictionary representation of square"""

        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
