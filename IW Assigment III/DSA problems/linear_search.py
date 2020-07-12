#Linear Search

def search(my_list, num):
    for i in range(len(my_list)):

        if my_list[i] == num:
            return i

    return -1


my_list = [5,8,2,1,9]
result = search(my_list, 1)
if result != -1:
    print(f"\nElement found on index {result}")
else:
    print("Elements not found")