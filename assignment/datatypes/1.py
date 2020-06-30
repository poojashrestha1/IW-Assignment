#Write a Python program to count the number of characters (character frequency) in a string.

string = "google.com"

frequency = {}

for i in string:
    string_list = frequency.keys()
    if i in string_list:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)


