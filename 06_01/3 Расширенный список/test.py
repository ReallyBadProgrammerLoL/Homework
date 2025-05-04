import unittest
from extList import ExtList

class TestExtList(unittest.TestCase):
    def test_head(self):
        obj = ExtList(1, 2, 3, 4, 5)
        self.assertEqual(obj.head(0), 1)
        self.assertEqual(obj.head(), 1)
        self.assertEqual(obj.head(1), 1)
        self.assertEqual(obj.head(3), [1, 2, 3])

    def test_head_error(self):
        obj = ExtList(1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            obj.head(-1)
        with self.assertRaises(IndexError):
            obj.head(85)

    def test_tail(self):
        obj = ExtList(1, 2, 3, 4, 5)
        self.assertEqual(obj.head(0), [2, 3, 4, 5])
        self.assertEqual(obj.head(), [2, 3, 4, 5])
        self.assertEqual(obj.head(1), [2, 3, 4, 5])
        self.assertEqual(obj.head(3), [1, 2, 3])

    def test_tail_error(self):
        obj = ExtList(1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            obj.head(-1)
        with self.assertRaises(IndexError):
            obj.head(85)


if __name__ == "__main__":
    unittest.main(argv=['f'], verbosity= 2)
