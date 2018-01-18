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
    else:
        raise TypeError("xrange expected at most 3 arguments, got %s" % len(args))

    if step>0:
        while current < high:
            old=current
            current+=step
            yield old
    else:
        while current>0:
            old=current
            current+=step
            yield old

if __name__ == '__main__':
    print(list(xrange(10)))
    print(list(xrange(2, 20)))
    print(list(xrange(0, 20, 2)))
    print(list(xrange(-10, 0, 1)))
    print(list(xrange(10 , 2)))
    print(list(xrange(0, 10, 2)))
    print(list(xrange(-10)))
    #print(list(xrange(10, 0, -1)))
    #print(list(xrange(0, 10, 2)))




    #print(list(xrange(10, 0, -1)))

