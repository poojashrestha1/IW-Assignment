#​ Write a Python program to count the occurrences of each word in a given sentence.
string = "This is the is best is is"

frequency = {}

for i in string.split(' '):
    string_list = frequency.keys()
    if i in string_list:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)
