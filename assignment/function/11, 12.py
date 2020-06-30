#Write a Python program to create a lambda function that adds 15 to a given
#number passed in as an argument, also create a lambda function that multiplies
#argument x with argument y and print the result.

sum = lambda a, b=15: a+b
total = sum(15)
print(total)

mul = lambda a,b: a*b
tiply = mul(5,5)
print(tiply)


#12
#Write a Python program to create a function that takes one argument, and
#that argument will be multiplied with an unknown given number.

def mul(x, y=12):
    result = x*y
    return result

print("The result is:", mul(10))
