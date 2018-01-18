
def unique(mylst):
    for i, x in enumerate(mylst):
        if x not in mylst[0:i]:
            yield x


if __name__ == '__main__':
    lst = [1, 2, 0, 1, 4, 1, 0, 5, 2]
    ret = list(unique(lst))
    print(ret == [1, 2, 0, 4, 5])
    lst1 = []
    l1 = list(unique([]))
    print(l1)

