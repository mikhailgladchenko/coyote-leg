class Matrix:
    def __init__(self, matrix_list):
        self.rows = matrix_list


    def __str__(self):
        return '\n'.join(' '.join(map(str, sl)) for sl in self.rows)

    def __eq__(self, other):
        return self.rows == other.rows

    def __add__(self, other):
        m = Matrix([])
        n = len(self.rows)
        rows = [[0]*n for x in range(n)]
        for i in range(n):
            for j in range(n):
                rows[i][j] = self.rows[i][j] + other.rows[i][j]
                m.rows = rows
        return m

    def __mul__(self, other):
        ro = len(other.rows)
        co = len(other.rows[0])
        cs = len(self.rows[0])
        rs = len(self.rows)

        m = Matrix.zeros(ro, co)
        if ro != cs:
            raise ValueError("cannot multiply matrices with not matching columns and rows")
        else:
            for i in range(rs):
                for j in range(co):
                    summa = 0
                    for k in range(cs):
                        summa = summa+self.rows[i][k]*other.rows[k][j]
                        m.rows[i][j] = summa
        return m

    @staticmethod
    def zeros(r, c):
        m = Matrix([])
        rows = [[0]*c for x in range(r)]
        m.rows = rows
        return m

    @staticmethod
    def identity(r, c):
        if r != c:
            raise ValueError("cannot create identity for not squared matrix")
        else:
            m = Matrix.zeros(r, c)
            for i in range(r):
                m.rows[i][i] = 1
        return m


def main():

    la = [[1, 3], [2, 5]]
    lb = [[1, 0], [0, 1]]
    lc = [[1, 3], [2, 5]]
    ld = [[2, 3], [2, 6]]
    le = [[1, 2, 3], [4, 5, 6]]
    lf = [[13, 17, 21], [22, 29, 36]]
    a = Matrix(la)
    print(str(a))
    b = Matrix(lb)
    print(str(b))
    c = Matrix(lc)

    d = Matrix(ld)

    e = Matrix(le)

    f = Matrix(lf)

    m = a*e

    z = Matrix.zeros(3, 3)
    print(str(z))
    i = Matrix.identity(3, 3)
    print(str(i))
    print("a*b=a"+":"+str(a*b == a))
    print("b*b=b"+":"+str(b*b == b))
    print("b*e=f" + ":" + str(a*e == f))
    print("a+b=d" + ":" + str(a+b == d))


if __name__ == '__main__':
    main()

