
def unique(mylist):
    dict_unique = {}
    for el in [dict_unique.setdefault(e, e) for e in mylist if e not in dict_unique]:
        yield el


if __name__ == '__main__':
    lst = [1, 2, 0, 1, 4, 1, 0, 5, 2]
    ret = list(unique(lst))
    print(ret == [1, 2, 0, 4, 5])
    lst1 = []
    l1 = list(unique([]))
    print(l1)

