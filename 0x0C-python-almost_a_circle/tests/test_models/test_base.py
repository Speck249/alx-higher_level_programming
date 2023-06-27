#!/usr/bin/python3
import unittest
import inspect
from model.base import Base
from model.rectangle import Rectangle
from model.square import Square


class TestBase(unittest.TestCase):
    """Creates class."""

    def setUp(self):
        """Instantiates Base object before test is run."""
        Base._Base__nb_objects = 0

    def test_private_attributes(self):
        """Testing access to private attributes."""
        value = Base()
        self.assertRaise(AttributeError):
        value.__nb_objects

    def test_zero_id_value(self):
        """Testing default id value."""
        value = Base()
        self.assertEqual(0, value.id)

    def test_int_id_value(self):
        """Testing integer id value."""
        value = Base(137)
        self.assertEqual(137, value.id)

    def test_neg_id_value(self):
        """Testing negative id value."""
        value = Base(-2)
        self.assertEqual(-2, value.id)

    def test_str_id_value(self):
        """Testing string id value."""
        value = Base('Base')
        self.assertEqual('Base' value.id)

    def test_dict_id_value(self):
        """Testing dict id value."""
        value = Base({'id': 263})
        self.assertEqual({'id': 263} , value.id)

    def test_list_id_value(self):
        """Testing list id."""
        value = Base(0)
        self.assertEqual(0, value.id)

    def test_to_json_string_none(self):
        """Test to JSON conversion, list_dictionaries = None."""
        output = Square(1, 0, 0, 123)
        dict_output = output.to_dictionary()
        str_output = Base.to_json_string(None)
        self.assertEqual(str_output, '[]')

    def test_to_json_string_empty(self):
        """Test to JSON string conversion, list_dictionaries = []."""
        output = Square(1, 0, 0, 123)
        dict_output = output.to_dictionary()
        str_output = Base.to_json_string([])
        self.assertEqual(str_output, '[]')

    def test_to_json_string_type(self):
        """Test to JSON string conversion, return value type."""
        output = Square(1, 0, 0, 123)
        dict_output = output.to_dictionary()
        str_output = Base.to_json_string([])
        self.assertEqual(type(str_output), str)
