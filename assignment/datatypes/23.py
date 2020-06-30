#Write a Python program to check a list is empty or not.



empty = []

def list_check(lists):
    if lists == empty:
        print("It is empty")
    else:
        print(lists)

list_check([])
list_check(['a','c'])
