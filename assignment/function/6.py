#Write a Python function to check whether a number is in a given range.

def in_range(number):
    if number in range(1, 25):
        print("Yes, it is.")
    else:
        print("No, it is not included.")

number = 25
in_range(number)