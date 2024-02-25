from models.base import Base
import unittest


class test_id(unittest.TestCase):

    def test_no_arg(self):
        self.obj1 = Base()
        self.obj2 = Base()
        self.assertEqual(self.obj1.id, self.obj2.id - 1)

    def test_scope(self):
        self.obj1 = Base(12)
        self.obj1.id = 2
        self.assertEqual(self.obj1.id, 2)

    def test_many_id(self):
        self.obj1 = Base()
        self.obj2 = Base()
        self.obj3 = Base()
        self.assertEqual(self.obj1.id, self.obj3.id - 2)

    def test_None_arg(self):
        self.obj1 = Base(None)
        self.obj2 = Base(None)
        self.assertEqual(self.obj1.id, self.obj2.id - 1)

    def test_with_arg(self):
        self.obj1 = Base(12)
        self.assertEqual(self.obj1.id, 12)

    def test_mix(self):
        self.obj1 = Base()
        self.obj2 = Base(12)
        self.obj3 = Base()
        self.assertEqual(self.obj1.id, self.obj3.id - 1)
