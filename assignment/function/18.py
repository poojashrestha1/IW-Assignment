#Write a Python program to check whether a given string is number or not

string = "47788"
another_string= "64dfd6"

start = lambda x: True if x.isdigit() else False
print(start(string))
print(start(another_string))
