#Write a Python program to remove an item from a tuple.

tuples = ('a', 'b', 'c')
lists = list(tuples)
print(type(lists))
print(lists)

i = input("Enter the index of the item:")
i = int(i)
new = lists.pop(i)

print(lists)