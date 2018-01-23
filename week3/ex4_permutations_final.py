def perm(lst):
    if len(lst) == 0:
        yield ()
    elif len(lst) == 1:
        yield (lst[0],)
    else:
        for i in range(len(lst)):
            x = lst[i]
            xt = lst[:i] + lst[i+1:]
            for j in perm(xt):
                yield tuple([x])+tuple(j)


if __name__ == '__main__':
    for p in perm([1, 2, 3]):
        print(p)
    for p in perm([]):
        print(p)
    for p in perm([1]):
        print(p)
