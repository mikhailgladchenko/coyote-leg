import unittest
from  ex1_done import *

class TestUrlMethods(unittest.TestCase):
    def test_url_empty(self):
        self.assertEqual(parse_url(""), None)

    def test_url_not_empty1(self):
        self.assertEqual(parse_url("page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc"), "foo=bar&page=2&x=y")
    def test_url_not_empty2(self):
        self.assertEqual(parse_url("apple=2&axile=bar&abbey=y&utm_source=ss&utm_content=ccc"),"abbey=y&apple=2&axile=bar")



if __name__ == '__main__':
    unittest.main()
