#Write a Python function to insert a string in the middle of a string.

def insert(to_string, string):
    index = len(to_string)/2
    it = int(index)
    print(type(it))
    new = to_string[:it] + string + to_string[it:]
    print(new)

insert("[[]]<<>>","Python")
