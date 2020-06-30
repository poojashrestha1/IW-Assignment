#Write a Python program to find if a given string starts with a given character
#using Lambda.

string = "My name is Pooja"

start = lambda x: True if x.startswith('M') else False
print(start(string))

#Reference from w3resources