# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'


def donuts(count):
    ret = "number of donuts:"
    if count < 10:
        ret = ret+str(count)
    else:
        ret = ret+"many"
    return ret
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.


def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[0:2]+s[-2:]
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):
    if len(s) <= 1:
        return ""
    else:
        first = s[0]
        last = s[1:]
        return first + last.replace(first, "*")
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    a_new = b[0:2]+a[2:]
    b_new = a[0:2]+b[2:]
    return a_new+" "+b_new


def my_test(got, expected):
    if got == expected:
        print("Pass")
    else:
        print("Fail")
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.


def test(got, expected):
        if got == expected:
            prefix = ' OK '
        else:
            prefix = '  X '
        print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    my_test(donuts(5), "number of donuts:5")
    my_test(donuts(50), "number of donuts:many")
    my_test(donuts(50), "number of donuts:50")
    my_test(both_ends("mikhailgladchenko"), "miko")
    my_test(both_ends("mikhailgladchenko"), "komi")
    my_test(both_ends("m"), "")
    my_test(both_ends("m"), "m")
    my_test(fix_start("oloko"), "ol*k*")
    my_test(fix_start("o"), "")
    my_test(fix_start("donut"), "donut")

    my_test(mix_up("mix", "pod"), "pox mid")
    my_test(mix_up("mix", "pod"), "pox mud")
    my_test(mix_up("gnash", "sport"), "spash gnort")
    my_test(mix_up("pezzy", "firm"), "fizzy perm")
    test(donuts(5), "number of donuts:5")
    test(donuts(50), "number of donuts:many")
    test(donuts(50), "number of donuts:50")


if __name__ == '__main__':
    main()
