import unittest
from week3.ex1_xrange_iterator import Xrange


class TestxrangeIterator(unittest.TestCase):
    def test_xrange_list(self):
        self.assertEqual(list(Xrange(0, 10)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_xrange_list1(self):
        self.assertEqual(list(Xrange(0, 10, 2)), [0, 2, 4, 6, 8])

    def test_xrange_list2(self):
        self.assertEqual(list(Xrange(-10, 0)), [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])

    def test_xrange_single(self):
        self.assertEqual(list(Xrange(1, 1)), [])

    def test_xrange_join(self):
        self.assertEqual(",".join(str(i) for i in Xrange(0, 10)), "0,1,2,3,4,5,6,7,8,9")

    def test_exception1(self):
        it = Xrange(1)
        next(it)
        with self.assertRaises(StopIteration):
            next(it)

    def test_exception2(self):
        with self.assertRaises(TypeError):
            print(list(Xrange(0, 1, 0.1)))

    def test_exception3(self):
        with self.assertRaises(TypeError):
            print(list(Xrange(1, 10, 2, 2)))

    def test_xrange_list4(self):
        self.assertEqual(list(Xrange(1)), [0])

    def test_xrange_list5(self):
        self.assertEqual(list(range(10, 0, -1)), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_xrange_list6(self):
        self.assertEqual(list(range(-10, 0)), [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])

    def test_xrange_list7(self):
        self.assertEqual(list(range(-10)), [])

    def test_xrange_yan1(self):
        self.assertEqual(list(Xrange(10, 122, -3)), list(range(10, 122, -3)))
    def test_xrange_yan3(self):
        self.assertEqual(list(Xrange(-10, -20, -1)), list(range(-10, -20, -1)))

    def test_exception4(self):
        with self.assertRaises(ValueError):
            print(list(Xrange(122, -10, 0)))

if __name__ == '__main__':
    unittest.main()
