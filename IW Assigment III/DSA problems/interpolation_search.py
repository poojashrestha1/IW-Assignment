#Interpolation Search

def interpolation(my_list, length, num):

    low = 0
    high = (length - 1)

    while low <= high and my_list[low] <= num <= my_list[high]:
        if low == high:
            if my_list[low] == num:
                return low
            return -1

        position = low + int(((float(high - low) / (my_list[high] - my_list[low])) * (num - my_list[low])))
        position = int(position)

        if my_list[position] == num:
            return position

        elif my_list[position] < num:
            low = position + 1

        else:
            high = position - 1

    return -1


my_list = [-8, 1, 25, 99,108]
length = len(my_list)

num = 99
index = interpolation(my_list, length, num)

if index != -1:
    print(f"\n{num} found at index {index}\n")
else:
    print(f"'n{num} not found\n")