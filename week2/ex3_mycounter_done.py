class MyCounter:

    def __init__(self, values=None):

        if values is not None:
            self.mydict = dict.fromkeys(values, 0)
            for value in values:
                self.mydict[value] += 1
        else:
            self.mydict = {}

    def __repr__(self):
        return repr(self.mydict)

    def most_common(self, n):
        sorted_items = sorted(self.mydict.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_items[:n]

    def elements(self):
        return self.mydict.keys()


def main():
    words = 'the lazy fox jumps over the brown dog and the brown cat'
    print(words)
    emptycnt = MyCounter()
    print(emptycnt)
    cnt = MyCounter(words.split())
    print(cnt)
    print(cnt.most_common(3))


if "__main__" == __name__:
    main()
