def xrange(*args):
    for arg in args:
        if not (isinstance(arg, int)):
            raise TypeError("object cannot be interpreted as an integer")
    current = 0
    high = 0
    step = 1
    if len(args) == 1:

        current = 0
        high = args[0]

    elif len(args) == 2:

        current = args[0]
        high = args[1]

    elif len(args) == 3:
        current = args[0]
        high = args[1]

        step = args[2]
        if step == 0:
            raise ValueError("xrange() arg 3 must not be zero")
    else:
        raise TypeError("xrange expected at most 3 arguments, got %s" % len(args))

    if step>0:
        while current < high:
            yield current
            current+=step

    else:
        while current>high:
            yield current
            current+=step


if __name__ == '__main__':
    print(list(xrange(10)))
    print(list(xrange(2, 20)))
    print(list(xrange(0, 20, 2)))
    print(list(xrange(-10, 0, 1)))
    print(list(xrange(10 , 2)))
    print(list(xrange(0, 10, 2)))
    print(list(xrange(-10)))
    print(list(xrange(-10, -20, -1)))
    print(list(xrange(10, 122, -3)))
    #print(list(xrange(10, 0, -1)))
    #print(list(xrange(0, 10, 2)))




    #print(list(xrange(10, 0, -1)))

