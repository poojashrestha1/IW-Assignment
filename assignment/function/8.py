#Write a Python function that takes a list and returns a new list with unique
#elements of the first list.

def unique_list(demolist):
    unique = set(demolist)
    return unique

demolist = [1,2,3,4,4,4,4,8,8,9]
print(list(unique_list(demolist)))