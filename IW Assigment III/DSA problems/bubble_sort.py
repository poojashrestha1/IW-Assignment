


def sorting(lists):
    
    for i in range(length-1):
        for j in range(length-i-1):

            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]

my_list = [5,8,2,1,9]
print("Original: ", my_list)
length = len(my_list)

sorting(my_list)

print(f"Sorted: {my_list}")

