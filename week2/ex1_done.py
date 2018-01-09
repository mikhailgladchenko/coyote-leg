# 1.	Write a function that will parse a url query string like "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc" and return a query string where all the params are sorted by their names like this "foo=bar&page=2&x=y" and all the "utm_" parameters are removed.

import unittest


def parse_url(url):
    if url == "":
        return None
    else:
        string_splitted = url.split("&")
        filtered = [x for x in string_splitted if not x.startswith("utm_")]
        sorted_alpha = sorted(filtered, key=lambda k: k[0])
        url_new = "&".join(sorted_alpha)
        return url_new


class TestUrlMethods(unittest.TestCase):
    def test_url_empty(self):
        self.assertEqual(parse_url(""), None)

    def test_url_not_empty(self):
        self.assertEqual(parse_url("page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc"), "foo=bar&page=2&x=y")


if __name__ == '__main__':
    unittest.main()
