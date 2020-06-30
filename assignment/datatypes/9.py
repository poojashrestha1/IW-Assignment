#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

string = "insight"

first = string[0]
last = string[-1]


length = len(string)
new_string = last + string[1:length-1] + first
print("Original = ", string)
print("New = ",new_string)