#Write a Python program to sort a list of tuples using Lambda.

sort = lambda list: sorted(list)
list = sort([(2,5), (1,9), (1,1), (7,1,5,7)])
print("Sorted list: \n", list)



#Write a Python program to sort a list of dictionaries using Lambda.

dict = [
    {'name':'train', 'age':'13'},
    {'name':'puppy', 'age':'27'},
    {'name':'hen', 'age':'09'},
    ]

sorted_dict = sorted(dict, key = lambda i: i['age'])

print("\n Sorted dictionary", sorted_dict)