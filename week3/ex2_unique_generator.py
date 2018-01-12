
def unique(mylist=[]):
    set = {}
    unique_values=[]
    if mylist is not []:
        unique_values = [set.setdefault(e, e) for e in mylist if e not in set]
    i=0
    while i <len(unique_values):
        yield unique_values[i]
        i+=1


if __name__ == '__main__':
    lst = [1, 2, 0, 1, 4, 1, 0, 5, 2]
    l=list(unique(lst))
    print(l==[1,2,0,4,5])
    lst1=[]
    l1=list(unique([]))
    print(l1)

