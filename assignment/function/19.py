#Write a Python program to create Fibonacci series upto n using Lambda.

from functools import reduce
  
fibo = lambda x: reduce(lambda i, _: i+[i[-1]+i[-2]], range(x-2), [0, 1]) 
                                 
print(fibo(8)) 

#reference from geeksforgeeks