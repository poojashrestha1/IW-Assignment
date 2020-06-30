# 18.​ Write a Python program to get the largest number from a list.
# 19.​ Write a Python program to get the smallest number from a list.


def order(lists):
    new = sorted(lists)
    max = new[-1]
    min = new[0]
    print("The largest number:", max)
    print("The smallest number:", min)

order([4,545,455,2,55,4])