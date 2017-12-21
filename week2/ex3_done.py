# 3.	Elements counting. It refers to the sections 1.12 and 1.4-1.5 of the Python Cookbook. Implement the Counter class. It should only support operations like __iter__, __getitem__ and .most_common(n). Try to make it as efficient as possible in terms of performance. Think of an underlying data structure that should be used and also a base class.
import collections
import collections.abc


def _identity(s):
    """"
    Default mutator function.
    """
    return s


class CustomCounter(collections.abc.MutableMapping):
    """
    Overrides the 5 methods of a MutableMapping:
    __getitem__, __setitem__, __delitem__, __iter__, __len__

    ...and the 3 non-Mapping methods of Counter:
    elements, most_common, subtract
    """

    def __init__(self, values=None, *, mutator=_identity):
        self._mutator = mutator
        if values is None:
            self._counter = collections.Counter()
        else:
            values = (self._mutator(v) for v in values)
            self._counter = collections.Counter(values)
        return

    def __getitem__(self, item):
        return self._counter[self._mutator(item)]

    def __setitem__(self, item, value):
        self._counter[self._mutator(item)] = value
        return

    def __delitem__(self, item):
        del self._counter[self._mutator(item)]
        return

    def __iter__(self):
        return iter(self._counter)

    def __len__(self):
        return len(self._counter)

    def __repr__(self):
        return ''.join([
          self.__class__.__name__,
          '(',
          repr(dict(self._counter)),
          ')'
          ])

    def elements(self):
        return self._counter.elements()

    def most_common(self, n):
        return self._counter.most_common(n)

    def subtract(self, values):
        if isinstance(values, collections.abc.Mapping):
            values = {self._mutator(k): v for k, v in values.items()}
            return self._counter.subtract(values)
        else:
            values = (self._mutator(v) for v in values)
            return self._counter.subtract(values)


def main():
    def mutator(s):
        # Asterisks are easier to print than '\ue000'.
        return '*' + s + '*'

    words = 'the lazy fox jumps over the brown dog'.split()

    # Test None (allowed by collections.Counter).
    ctr_none = CustomCounter(None)
    assert 0 == len(ctr_none)

    # Test typical dict and collections.Counter methods.
    ctr = CustomCounter(words, mutator=mutator)
    print(ctr)
    assert 1 == ctr['dog']
    assert 2 == ctr['the']
    assert 7 == len(ctr)
    del(ctr['lazy'])
    assert 6 == len(ctr)
    ctr.subtract(['jumps', 'dog'])
    assert 0 == ctr['dog']
    assert 6 == len(ctr)
    ctr.subtract({'the': 5, 'bogus': 100})
    assert -3 == ctr['the']
    assert -100 == ctr['bogus']
    assert 7 == len(ctr)
    return


if "__main__" == __name__:
    main()




