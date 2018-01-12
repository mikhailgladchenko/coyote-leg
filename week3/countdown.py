class countdown:
    def __init__(self, n):
        self.end = n
        self.current= n
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0 :
            raise StopIteration
        else:
            old = self.current
            self.current -=1
            return old

if __name__ == '__main__':
    c=countdown(5)
    for i in c:
        for j in c:
            print(i,j)
