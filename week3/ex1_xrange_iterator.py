
class xrange:
    def __init__(self, *args):

        for i in list(args):
            if not(isinstance(i,int)):
                raise TypeError("object cannot be interpreted as an integer")
        if len(args) == 1:

            self.current = 0
            self.high = args[0]
            self.step = 1
        elif len(args) == 2:
            self.current = args[0]
            self.high = args[1]
            self.step = 1
        elif len(args) == 3:
            self.current = args[0]
            self.high = args[1]
            self.step = args[2]
        else:
            raise TypeError("xrange expected at most 3 arguments, got %s" % len(args))

    def __iter__(self):
        return self

    def __next__(self):
        #added this check additionally
        if self.current < self.high and self.step < 0:
            raise StopIteration

        if self.current >= self.high:
            raise StopIteration
        else:
            old = self.current
            self.current += self.step
            return old


if __name__ == '__main__':
    print(list(xrange(10)))
    r4 = range(10, 0, -1)
    print(list(r4))
    r5 = range(-10, 0)
    print(list(r5))
    print(list(xrange(-10)))
    print(list(xrange(10,122,-3)))



