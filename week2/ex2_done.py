# 2.	Write a function that will parse a url query string like "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc" and return a query string where all the params retain their original order "page=2&foo=bar&x=y" and all the "utm_" parameters are removed.

import unittest


def parse_url(url):
    if url == "":
        return None
    else:
        string_splitted = url.split("&")
        filtered = [x for x in string_splitted if not x.startswith("utm_")]

        url_new = "&".join(filtered)
        return url_new


class TestUrlMethods(unittest.TestCase):
    def test_url_empty(self):
        self.assertEqual(parse_url(""), None)

    def test_url_not_empty1(self):
        self.assertEqual(parse_url("page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc"), "page=2&foo=bar&x=y")

    def test_url_not_empty2(self):
        self.assertEqual(parse_url("apple=2&axile=bar&abbey=y&utm_source=ss&utm_content=ccc"), "apple=2&axile=bar&abbey=y")


if __name__ == '__main__':
    unittest.main()
