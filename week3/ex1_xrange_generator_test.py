import unittest
from week3.ex1_xrange_generator import xrange


class TestxrangeIterator(unittest.TestCase):
    def test_xrange_list(self):
        self.assertEqual(list(xrange(0, 10)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_xrange_list1(self):
        self.assertEqual(list(xrange(0, 10, 2)),[0,2,4,6,8])
    def test_xrange_list2(self):
        self.assertEqual(list(xrange(-10,0)), [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1])

    def test_xrange_single(self):
        self.assertEqual(list(xrange(1,1)),[])
    def test_xrange_join(self):
        self.assertEqual(",".join(str(i) for i in xrange(0,10)),"0,1,2,3,4,5,6,7,8,9")
    def test_xrange_list4(self):
        self.assertEqual(list(xrange(10,0,-1)),[10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    def test_exception1(self):
        with self.assertRaises(TypeError):
            ret = list(xrange(0, 1, 0.1))
    def test_exception2(self):
        with self.assertRaises(TypeError):
            ret = list(xrange(0, 10,2, 2 ))
    def test_xrange_list5(self):
        self.assertEqual(list(xrange(10,0,-1)),[10,9, 8, 7, 6, 5, 4, 3, 2, 1])
    def test_xrange_list6(self):
        self.assertEqual(list(xrange(10)),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_xrange_yan1(self):
        self.assertEqual(list(xrange(10,2)),list(range(10,2)))
if __name__ == '__main__':
    unittest.main()