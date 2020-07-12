#Quick sort

def partition(my_list, low, high):
    i = (low - 1)

    pivot = my_list[high]

    for j in range(low, high):

        if my_list[j] < pivot:
            i = i + 1
            my_list[i], my_list[j] = my_list[j], my_list[i]

    my_list[i + 1], my_list[high] = my_list[high], my_list[i + 1]
    return i + 1


def quick_sort(my_list, low, high):
    if low < high:
        parts = partition(my_list, low, high)
        quick_sort(my_list, low, parts - 1)
        quick_sort(my_list, parts + 1, high)


my_list = [5,8,2,1,9]
print("Original: ", my_list)

length = len(my_list)

quick_sort(my_list, 0, length-1)
print (f"Sorted: {my_list}") 