#Write a Python program to find intersection of two given arrays using Lambda.

array1 = [1,2,3,4,5,9]
array2 = [4,5,6,7,8,9]
intersect = lambda x : x in array1 and array2 
result = filter(intersect, array1 and array2)
print(list(result))