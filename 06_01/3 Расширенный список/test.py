import unittest
from extList import ExtList

class TestExtList(unittest.TestCase):
    def setUp(self):
        self.obj = ExtList(1, 2, 3, 4, 5)

    def test_head(self):
        self.assertEqual(self.obj.head(0), 1)
        self.assertEqual(self.obj.head(), 1)
        self.assertEqual(self.obj.head(1), 1)
        self.assertEqual(self.obj.head(3), [1, 2, 3])

    def test_head_error(self):
        with self.assertRaises(IndexError):
            self.obj.head(-1)
        with self.assertRaises(IndexError):
            self.obj.head(85)

    def test_tail(self):
        self.assertEqual(self.obj.tail(0), [2, 3, 4, 5])
        self.assertEqual(self.obj.tail(), [2, 3, 4, 5])
        self.assertEqual(self.obj.tail(1), [2, 3, 4, 5])
        self.assertEqual(self.obj.tail(2), [4, 5])

    def test_tail_error(self):
        with self.assertRaises(IndexError):
            self.obj.tail(-1)
        with self.assertRaises(IndexError):
            self.obj.tail(85)

    def test_last(self):
        self.assertEqual(self.obj.last(), 5)

    def test_add(self):
        new_list = self.obj + [6, 7]
        self.assertEqual(list(new_list), [1, 2, 3, 4, 5, 6, 7])

    def test_mul(self):
        new_list = self.obj * 2
        self.assertEqual(list(new_list), [1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

    def test_list_methods(self):
        self.obj.append(6)
        self.assertEqual(self.obj.last(), 6)

        self.obj.insert(0, 0)
        self.assertEqual(self.obj.head(2), [0, 1])

        self.obj.remove(3)
        self.assertNotIn(3, self.obj)

        count = self.obj.count(2)
        self.assertEqual(count, 1)

        index = self.obj.index(2)
        self.assertEqual(index, 2)

        copied = self.obj.copy()
        self.assertEqual(list(copied), list(self.obj))

        self.obj.pop()
        self.assertNotEqual(self.obj.last(), 6)

        self.obj.sort(reverse=True)
        sorted_list = sorted(self.obj, reverse=True)
        self.assertEqual(list(self.obj), sorted_list)

        self.obj.clear()
        self.assertEqual(len(self.obj), 0)

    def test_reverse(self):
        reversed_list = reversed(self.obj)
        self.assertEqual(list(reversed_list), [5, 4, 3, 2, 1])

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2)
