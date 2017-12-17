from operator import itemgetter
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.


def match_ends_with_lambda(words):
    length_list = list(filter(lambda x: len(x) >= 2, words))
    list_to_return = list(filter(lambda x: x[0] == x[-1], length_list))
    return len(list_to_return)


def match_ends_without_lambda(words):
    list_to_return = []
    for word in words:
        if (len(word) >= 2) and (word[0] == word[-1]):
            list_to_return.append(word)
    return len(list_to_return)


def my_test(got, expected):
    if got == expected:
        print("Pass")
    else:
        print("Fail")

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.


def front_x_with_lambda(words):
    list_with_x = list(filter(lambda x: (x.startswith("x")), words))
    other_list = list(filter(lambda x: (not x.startswith("x")), words))
    return sorted(list_with_x)+sorted(other_list)


def front_x_without_lambda(words):
    list_with_x = []
    other_list = []
    for word in words:
        if word.startswith("x"):
            list_with_x.append(word)
        else:
            other_list.append(word)

    return sorted(list_with_x)+sorted(other_list)

# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.


def sort_last_with_lambda(tuples):
    return sorted(tuples, key=lambda k: k[-1])


def sort_last_without_lambda(tuples):
    return sorted(tuples, key=itemgetter(-1))


def main():
    my_test(match_ends_with_lambda(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends_with_lambda(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    my_test(match_ends_without_lambda(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends_without_lambda(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    my_test(match_ends_with_lambda(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends_with_lambda(['', 'x', 'xy', 'xyx', 'xx']), 2)
    my_test(match_ends_with_lambda(['aaa', 'be', 'abc', 'hello']), 1)
    test(match_ends_with_lambda(['aaa', 'be', 'abc', 'hello']), 1)
    my_test(match_ends_without_lambda(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends_without_lambda(['', 'x', 'xy', 'xyx', 'xx']), 2)
    my_test(match_ends_without_lambda(['aaa', 'be', 'abc', 'hello']), 1)
    test(match_ends_without_lambda(['aaa', 'be', 'abc', 'hello']), 1)
    my_test(front_x_with_lambda(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x_with_lambda(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])

    got = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    expected = ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    my_test(front_x_with_lambda(got), expected)
    got1 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    expected1 = ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    test(front_x_with_lambda(got1), expected1)
    my_test(sort_last_with_lambda([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    test(sort_last_with_lambda([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    my_test(sort_last_with_lambda([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    my_test(sort_last_without_lambda([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    test(sort_last_without_lambda([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    my_test(sort_last_without_lambda([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    test(sort_last_without_lambda([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
