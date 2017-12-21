"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""
import sys


def get_dictionary(filename):
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        words_dict = dict.fromkeys(words, 0)
        for word in words:
            words_dict[word] += 1
        return words_dict


def print_words(filename):
    words_dict = get_dictionary(filename)
    sorted_keys_list = sorted(words_dict.keys())
    for key in sorted_keys_list:
        print(key + ":"+str(words_dict[key]))


def print_top(filename):
    words_dict = get_dictionary(filename)
    sorted_keys_list = sorted(words_dict.keys())
    tuple_to_add = ()
    list_to_sort = []
    for key in sorted_keys_list:
        tuple_to_add = (key, words_dict[key])
        list_to_sort.append(tuple_to_add)
    sorted_by_second = sorted(list_to_sort, key=lambda tup: tup[1], reverse=True)
    top10 = sorted_by_second[:10]
    for tentry in top10:
        print(tentry[0] + ":" + str(tentry[1]))


def main():

    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)
    else:
        option = sys.argv[1]
        filename = sys.argv[2]
    if option == "--count":
        print_words(filename)
    else:
        print_top(filename)


if __name__ == '__main__':
    main()
