#​ Write a Python program that accepts a comma separated sequence of words
#as input and prints the unique words in sorted form (alphanumerically).

words = input('Enter some words:')

new = set(words.split(','))

string = sorted(new)
print("Sorted: " + ','.join(string))

