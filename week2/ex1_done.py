# 1.	Write a function that will parse a url query string like "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc" and return a query string where all the params are sorted by their names like this "foo=bar&page=2&x=y" and all the "utm_" parameters are removed.

import unittest


def parse_url(url):

    string_splitted = url.split("&")
    params_dict = {}
    filtered = [x for x in string_splitted if not x.startswith("utm_")]
    for entry in filtered:
        key = value = ""
        try:
            key = entry.split("=")[0]
            value = entry.split("=")[1]
        except IndexError:
            pass

        params_dict[key] = value
    keys_sorted = sorted(params_dict.keys())
    url_new = "&".join(["%s=%s" % (k, params_dict[k]) for k in keys_sorted])

    if url_new == str("="):
        return None
    else:
        return url_new

    # for key in keys_sorted:
    #
    #     new_url += "{}={}{}".format(key, params_dict[key], "&")

    # if url_new== str("="):
    #     return None
    # else:
    #     return url_new


class TestUrlMethods(unittest.TestCase):
    def test_url_empty(self):
        self.assertEqual(parse_url(""), None)

    def test_url_not_empty(self):
        self.assertEqual(parse_url("page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc"), "foo=bar&page=2&x=y")


if __name__ == '__main__':
    unittest.main()
