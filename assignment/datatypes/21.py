#Write a Python program to get a list, sorted in increasing order by the last
#element in each tuple from a given list of non-empty tuples.


def last(n):
    return n[-1]

def sort(sorting):
    sort = sorted(sorting, key = last)
    return sort

print("Sorted list: ", sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


