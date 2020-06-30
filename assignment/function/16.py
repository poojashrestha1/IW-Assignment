#Write a Python program to square and cube every number in a given list of
#integers using Lambda.


numbers = [1,2,3,4,5]

sqr = lambda x: x**2
cubes = lambda x: x**3
sqr_result = map(sqr,numbers)
cubes_result = map(cubes,numbers)
print("The squares are: ", list(sqr_result))
print("The cubes are: ", list(cubes_result))