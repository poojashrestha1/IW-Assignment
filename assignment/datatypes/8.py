#​ Write a Python program to remove the n​ th​ index character from a nonempty string.

string = "Python"
index = 4

if string == "":
    print("It is empty")
else:
    for i in string:
        if string.find(i) == index:
            print(string[:index] + string[index+1:])

