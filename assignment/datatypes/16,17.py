#Write a Python program to sum all the items in a list.

def result(lists):
    sums = 0
    mul = 1
    
    for i in lists:
        sums = sums + i
        mul = mul * i
    print("Sum is : ", sums)
    print("Multiplies : ", mul)

result([1,2,3,4,5])
    