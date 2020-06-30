#1

#Write a Python function to find the Max of three numbers.

def maximum(num1, num2, num3):
    if num1>num2 and num1>num3:
        max = num1
    elif num2>num1 and num2>num3:
        max = num2
    else:
        max = num3

    return max

num1, num2, num3 = input("Enter a three value: ").split() 
print(maximum(num1, num2, num3))