#!/usr/bin/python3
"""
Unittest for Base class
"""

import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """
    Base class test

    Args:
        unittest ([type]): Module to do test
    """
    def test_id(self):
        """
        Test with positive IDs
        """
        O1 = Base()
        self.assertEqual(O1.id, 1)
        O2 = Base()
        self.assertEqual(O2.id, 2)
        O3 = Base(43)
        self.assertEqual(O3.id, 43)

    def test_negativ_id(self):
        N1 = Base(-6)
        self.assertEqual(N1.id, -6)
        N2 = Base((-6 + 2))
        self.assertEqual(N2.id, -4)

    def test_raise(self):
        """
        Trying more arguments
        """
        with self.assertRaises(TypeError):
            N3 = Base(1,3)

    def test_id_tuple_list(self):
        """
        Test with list as ID
        """
        N4 = Base([1,2])
        self.assertEqual(N4.id, [1,2])

    def test_is_none(self):
        Ob1 = Base()
        self.assertIsInstance(Ob1, Base)

if __name__ == "__main__":
    unittest.main()
