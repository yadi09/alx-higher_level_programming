import unittest
max_int = __import__('6-max_integer').max_integer


class TestMax_integer(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_int(), None)

    def test_int_list(self):
        l = [10, 32, 1, 100, 0]
        self.assertEqual(max_int(l), 100)

    def test_float_list(self):
        l = [10.34535, 2.234, 10.346]
        self.assertEqual(max_int(l), 10.346)
