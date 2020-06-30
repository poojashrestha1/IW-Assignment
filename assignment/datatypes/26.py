#Write a Python program to insert a given string at the beginning of all items in a list.

def insert(lists):
    string = 'abc'
    for i in range(len(lists)):
        lists[i] = string + str(lists[i])
    return lists


print(insert([1, 2, 3, 4]))

