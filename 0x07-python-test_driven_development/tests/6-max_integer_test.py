import unittest
max_int = __import__('6-max_integer').max_integer


class TestMax_integer(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_int(), None)

    def test_max_end(self):
        l = [10, 32, 1, 100]
        self.assertEqual(max_int(l), 100)

    def test_max_beginning(self):
        l = [100, 23, 3, 0]
        self.assertEqual(max_int(l), 100)

    def test_max_middle(self):
        l = [1, 23, 100, 2, 0]
        self.assertEqual(max_int(l), 100)

    def test_with_negative(self):
        l = [1, -23, 100, 0]
        self.assertEqual(max_int(l), 100)

    def test_only_negative(self):
        l = [-12, -43, -100, -1]
        self.assertEqual(max_int(l), -1)

    def test_one_element(self):
        l = [10]
        self.assertEqual(max_int(l), 10)
