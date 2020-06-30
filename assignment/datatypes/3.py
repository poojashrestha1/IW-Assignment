#Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.

string = "stringsss"

toreplace = string[0]
for i in string:
    if i == toreplace:
        new_string = string.replace(toreplace, '$')
        new_string = toreplace + new_string[1:]
print(new_string)