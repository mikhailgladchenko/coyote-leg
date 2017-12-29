# 4.	Implement a class User with attributes name, age. The instances of this class should be sortable by age by default. So sorted([User(name='Eric', age=34), User(name='Alice', age=22)]) will return a list of sorted users by their age (ASC). How would you sort those objects by name? Don't forget to Implement __str__ method to help testing and visualize the object.
# Hint for the default sorting: __cmp__, functools.total_ordering.
#

from functools import total_ordering


@total_ordering
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "%s %s" % (self.name, self.age)

    def __eq__(self, other):
        return (self.namelast, self.age) == (other.name, other.age)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.age < other.age

    @staticmethod
    def cmp(x, y):
        return (x > y) - (x < y)

    def __cmp__(self, other):
        return User.cmp(self.age, other.age)


def main():
    users = [User("mikhail", 57), User("marina", 55), User("alexandra", 19), User("mikhail", 31)]
    print(users)
    sorted_users_by_age = sorted(users)
    print(sorted_users_by_age)
    sorted_users_by_name = sorted(sorted_users_by_age, key=lambda u: u.name)
    print(sorted_users_by_name)


if __name__ == '__main__':
        main()
