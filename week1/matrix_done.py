class Matrix:
    def __init__(self, list):
        self.rows= list
    def print(self):
        print('\n'.join(' '.join(map(str, sl)) for sl in self.rows))
    def __eq__(self,other):
        if self.rows==other.rows: return True
        else: return False
    def __add__(self, other):
       m=Matrix([])
       n=len(self.rows)
       rows=[[0]*n for x in range(n)]
       for i in range(0,n):
          for j in range(0,n): rows[i][j]=self.rows[i][j]+other.rows[i][j]
       m.rows=rows
       return m
    def __mul__(self, other):
        ro=len(other.rows)
        co=len(other.rows[0])
        cs=len(self.rows[0])
        rs=len(self.rows)
        #print("row count="+str(r))
        #print("colomn count=" + str(c))
        m=Matrix.Zeros(ro,co)
        if ro!=cs: raise ValueError("cannot multiply matrices with not matching columns and rows")
        else:
            for i in range(rs):
                for j in range(co):
                    sum=0
                    for k in range(cs):
                       sum=sum+self.rows[i][k]*other.rows[k][j]
                       m.rows[i][j]=sum
        return m
    @staticmethod
    def Zeros(r,c):
        m=Matrix([])
        rows = [[0]*c for x in range(r)]
        m.rows=rows
        return m
    @staticmethod
    def Identity(r,c):
        if r!=c: raise ValueError("cannot create identity for not squared matrix")
        else:
         m=Matrix.Zeros(r,c)
         for i in range(r):m.rows[i][i]=1
         return m

def main():
    print("testing-")
    la=[[1,3],[2,5]]
    lb=[[1,0],[0,1]]
    lc=[[1,3],[2,5]]
    ld=[[2,3],[2,6]]
    le=[[1,2,3],[4,5,6]]
    lf=[[13,17,21],[22,29,36]]
    a=Matrix(la)
    a.print()
    b=Matrix(lb)
    b.print()
    c=Matrix(lc)
    c.print()
    d=Matrix(ld)
    d.print()
    e=Matrix(le)
    e.print()
    f=Matrix(lf)
    f.print()
    m=a*e
    m.print()
    z=Matrix.Zeros(3,3)
    z.print()
    i=Matrix.Identity(3,3)
    i.print()
    print("a*b=a"+":"+str(a*b==a))
    print("b*b=b"+":"+str(b*b==b))
    print("b*e=f" + ":" + str(a*e == f))
    print("a+b=d" + ":" + str(a+b == d))
if __name__ == '__main__':
  main()


#i=Matrix.Identity(4,5)
#i.print()

#z=a.Zeros(3,3)
#z.print()

