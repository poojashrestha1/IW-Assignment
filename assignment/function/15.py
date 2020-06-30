#Write a Python program to filter a list of integers using Lambda.

numbers = [15,54,22,488,87,19]
even = lambda x: (x % 2) == 0 
odd = lambda x: (x % 2) != 0 
e_result = filter(even, numbers)
o_result = filter(odd, numbers)
print("Even numbers: ", list(e_result))
print("Odd numbers: ", list(o_result))



#reference from w3resource