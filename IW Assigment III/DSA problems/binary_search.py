#Binary Search

list_search = [-8, 1, 25, 99,108]


def binary_search(list_search, low, high, number):

    if(high>=low):
        mid  = (high + low) //2
        if number == list_search[mid]:
            return mid
        elif number < list_search[mid]:
            binary_search(list_search, low, mid-1, number)
        elif number > list_search[mid]:
            binary_search(list_search, low, mid+1, number)

    else:
        return -1

number = 25
index = binary_search(list_search, 0, len(list_search)-1, number)


if index == -1: 
    print("Not Found")

# is not functioning
    
else:
    print(f"\n{number} was found at index {index} ")