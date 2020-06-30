#Write a Python program to remove a key from a dictionary.

diction = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50}
keys = diction.keys()
print("The keys are: ", keys)
remove = input("Enter the key you want to remove: ")
diction.pop(remove)
print(diction)