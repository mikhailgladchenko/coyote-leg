import unittest
from week3.ex3_countdown import countdown


class TestxrangeIterator(unittest.TestCase):
    def test_countdown_list(self):
        c = countdown(5)
        lst = c.get_list(5)
        self.assertEqual(lst, [[5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 5], [3, 4], [3, 3], [3, 2], [3, 1], [2, 5], [2, 4], [2, 3], [2, 2], [2, 1], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1]])


if __name__ == '__main__':
    unittest.main()

