#Write a Python program to get a single string from two given strings, separated
#by a space and swap the first two characters of each string.

str1 = "this"
str2 = "ist"

first = str2[:2] + str1[2:]
second = str1[:2] + str2[2:]

result = first + " " + second

print(result)


