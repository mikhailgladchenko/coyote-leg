import unittest
from week3.ex2_unique_generator import unique


class TestUnique(unittest.TestCase):
    def test_unique1(self):
        self.assertEqual(list(unique([1, 2, 0, 1, 4, 1, 0, 5, 2])), [1, 2, 0, 4, 5])

    def test_empty(self):
        self.assertEqual(list(unique([])), [])


if __name__ == '__main__':
    unittest.main()
