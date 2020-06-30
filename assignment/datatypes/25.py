#Write a Python program to check whether all dictionaries in a list are empty or not.

def check_empty(lists):
    for dict in lists:
        if dict:
            return False
        else:
            return True

print(check_empty([{'4':45},{},{}]))
print(check_empty([{},{}]))
