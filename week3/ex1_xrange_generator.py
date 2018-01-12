def xrange(*args):
    for i in list(args):
        if not (isinstance(i,int)):
            raise TypeError("object cannot be interpreted as an integer")
    current = 0
    high = 0
    step = 1
    if len(args) == 1:

        current = 0
        high = args[0]
        step = 1
    elif len(args) == 2:
        current = args[0]
        high = args[1]
        step = 1 if current < high else -1
    elif len(args) == 3:
        current = args[0]
        high = args[1]
        step = args[2] if current < high else -1
    else:
        raise TypeError("xrange expected at most 3 arguments, got %s" % len(args))
    if current < high:
        while current < high:
            yield current
            current += step
    else:
        while high < current:
            yield current
            current += step


if __name__ == '__main__':
    print(list(xrange(10)))
    print(list(xrange(2, 20)))
    print(list(xrange(0, 20, 2)))
    print(list(xrange(-10, 0, 1)))
    print(list(xrange(10, 0, -1)))
    print(list(xrange(10, 0)))
