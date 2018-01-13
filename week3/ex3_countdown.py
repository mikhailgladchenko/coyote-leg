class countdown:

    def __init__(self, end):
        self.current = self.end = end

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            old = self.current
            self.current -= 1
            return old

    def __iter__(self):
        return countdown(self.end)

    def get_list(self, n):
        c = countdown(n)
        result = []
        for k in c:
            for l in c:
                result.append([k, l])
        return result


if __name__ == '__main__':
    r = countdown(5)
    for i in r:
        for j in r:
            print(i, j)
    ret = r.get_list(5)
    print(ret)

