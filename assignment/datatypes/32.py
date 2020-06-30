#Write a Python script to generate and print a dictionary that contains a
#number (between 1 and n) in the form (x, x*x).

num = input("Enter a number: ")
num = int(num)
dictionary = {}
for i in range(1, num + 1):
    dictionary[i] = i*i
print(dictionary)
