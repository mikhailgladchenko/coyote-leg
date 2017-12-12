def match_ends(words):
    n_list = list(filter(lambda x: (len(x) >= 2), words))
    r_list = list(filter(lambda x: (x[0]==x[-1]), n_list))
    return len(r_list)
def test(got,expected):
    if got==expected:
       print("Pass")
    else:
       print("Fail")
def front_x(words):
    x_list = list(filter(lambda x: (x.startswith("x")), words))
    r_list = list(filter(lambda x: (not x.startswith("x")), words))
    return sorted(x_list)+sorted(r_list)
def sort_last(tuples):
    return sorted(tuples,key=lambda k:k[-1])
def main():
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__ == '__main__':
  main()
