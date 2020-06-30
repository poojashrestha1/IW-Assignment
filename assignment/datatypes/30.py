#Write a Python script to check whether a given key already exists in a dictionary.

def search_key(dictionary, key):
    if key in dictionary.keys():
        print("Exists")
    else:
        print("Doesn't exist")

search_key({'name': 'apple', 'age': 24}, 'named')
search_key({'name': 'apple', 'age': 24}, 'age')