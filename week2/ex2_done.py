# 2.	Write a function that will parse a url query string like "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc" and return a query string where all the params retain their original order "page=2&foo=bar&x=y" and all the "utm_" parameters are removed.


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

    url_new = "&".join(["%s=%s" % (k, v) for k, v in params_dict.items()])

    if url_new == str("="):
        return None
    else:
        return url_new


def main():
    url = "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc"
    print(url)
    url_new = parse_url(url)
    print(url_new)
    print(parse_url(""))


if __name__ == '__main__':
    main()
