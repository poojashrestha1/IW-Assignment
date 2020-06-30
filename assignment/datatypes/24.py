#​ Write a Python program to clone or copy a list.

def copy(lists):
    copied = lists.copy()
    return copied

original = [1,23,5,6,7]
print("Original list:", original)
print("Copied list:", copy(original))


