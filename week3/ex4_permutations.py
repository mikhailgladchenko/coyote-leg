

def all_perms_generator(elements):
    if len(elements) <= 1:
        yield elements
    else:

        for perm in all_perms_generator(elements[1:]):

            for i in range(len(elements)):
                ret = tuple(perm[:i]) + tuple(elements[0:1]) + tuple(perm[i:])
                yield ret


def permutations(elements):
    """generates the list of permutations in the same manner as itertools.permutations does"""

    if elements == []:
        return [()]
    if len(elements) == 1:
        return [(elements[0],)]
    lst = []
    for p in all_perms_generator(elements):
        lst.append(p)
    return sorted(lst)


if __name__ == '__main__':
    print(permutations([1, 2, 3]))
    #print(permutations([]))
    #print(permutations([1]))
