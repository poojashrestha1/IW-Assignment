#Write a Python program to total_sum all the items in a dictionary.
#Write a Python program to multiply all the items in a dictionary.

diction = {"age1" : 12, "age2": 15}

diction_values = diction.values()
print(diction_values)

total_sum = 0
mul = 1
for i in diction_values:
    total_sum = total_sum + i
    mul = mul * i
print("Total Sum = ", total_sum)
print("Total multiplied = ", mul)