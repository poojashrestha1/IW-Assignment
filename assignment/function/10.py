#Write a Python program to print the even numbers from a given list.

def even_numbers(number_list):
    for i in number_list:
        if i % 2 == 0:
            print(i)

number_list = [1,2,3,4,5,6]
even_numbers(number_list)
