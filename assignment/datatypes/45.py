#Write a Python program to find the index of an item of a tuple.

tuplee = ('a', 'b', 'c')
print(tuplee)
item = input("Enter an item for an index: ")

find = tuplee.index(item)
print("Index: ", find)