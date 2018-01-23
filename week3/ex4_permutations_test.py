import unittest
from week3.ex4_permutations import permutations
import itertools


class TestPermutations(unittest.TestCase):
    def test_perms1(self):
        data = [1, 2, 3]
        self.assertEqual(list(permutations(data)), list(itertools.permutations(data)))

    def test_perms2(self):
        data = "123"
        self.assertEqual(list(permutations(data)), list(itertools.permutations(data)))

    def test_perms3(self):
        data = ["a", "b", "c"]
        self.assertEqual(list(permutations(data)), list(itertools.permutations(data)))

    def test_perms4(self):
        data = []
        self.assertEqual(list(permutations(data)), list(itertools.permutations(data)))

    def test_perms5(self):
        data = [1]
        self.assertEqual(list(permutations(data)), list(itertools.permutations(data)))


if __name__ == '__main__':
    unittest.main()
