#Write a Python function to calculate the factorial of a number (a non-negative
#integer). The function accepts the number as an argument.

def fact(number):
    factorial = 1
    for x in range(2, number+1):
        factorial = factorial * x
    return factorial


number = 5
print(fact(number))
