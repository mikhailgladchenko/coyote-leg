# 2.	Write a function that will parse a url query string like "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc" and return a query string where all the params retain their original order "page=2&foo=bar&x=y" and all the "utm_" parameters are removed.


def parse_url(url):
    string_splitted = url.split("&")
    params_dict = {}
    for entry in string_splitted:
        key = entry.split("=")[0]
        value = entry.split("=")[1]
        if "utm_" not in key:
            params_dict[key] = value
    keys_original = (params_dict.keys())
    new_url = ""

    for key in keys_original:

        new_url += "{}={}{}".format(key, params_dict[key], "&")

    return new_url[0:-1]


def main():
    url = "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc"
    print(url)
    url_new = parse_url(url)
    print(url_new)


if __name__ == '__main__':
    main()
