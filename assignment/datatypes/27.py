#Write a Python program to replace the last element in a list with another list.

def replace(list1, list2):
    new_list = list1[:-1] + list2
    print(new_list)

replace([1, 3, 5, 7, 9, 10], [2, 4, 6, 8])





