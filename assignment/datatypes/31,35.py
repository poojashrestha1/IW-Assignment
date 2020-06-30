#Write a Python program to iterate over dictionaries using for loops.

def display(dictionary):
    for i in dictionary.keys():
        for j in dictionary.values():
            print("Key:", i)
            print("Value:", j)
            print("\n")

display({'name': 'apple', 'age': 24})