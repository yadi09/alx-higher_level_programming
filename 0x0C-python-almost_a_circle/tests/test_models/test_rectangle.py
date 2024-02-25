from models.base import Base
from models.rectangle import Rectangle
import unittest


class testRectangle(unittest.TestCase):

    def setUp(self):
        self.r = Rectangle(10, 2)
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(10, 2, 7, 8, 12)

    def tearDown(self):
        del self.r1
        del self.r2

    def test_issubclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_two_arg(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r.id, self.r1.id - 1)

    def test_all_arg(self):
        self.assertEqual(self.r2.x, 7)
        self.assertEqual(self.r2.y, 8)
        self.assertEqual(self.r2.id, 12)

    def test_getter_setter_width(self):
        self.assertEqual(self.r1.width, 10)
        self.r1.width = 20
        self.assertEqual(self.r1.width, 20)

    def test_getter_setter_height(self):
        self.assertEqual(self.r1.height, 2)
        self.r1.height = 4
        self.assertEqual(self.r1.height, 4)

    def test_getter_setter_x(self):
        self.assertEqual(self.r2.x, 7)
        self.r2.x = 70
        self.assertEqual(self.r2.x, 70)

    def test_getter_setter_y(self):
        self.assertEqual(self.r2.y, 8)
        self.r2.y = 80
        self.assertEqual(self.r2.y, 80)
