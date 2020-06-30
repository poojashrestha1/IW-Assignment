#Write a Python function that takes a number as a parameter and check the
#number is prime or not.

def check_prime(number):
    if number > 1:
        for x in range(2, number):
            if (number % x) != 0:
                print("It is prime")
                break
            else:
                print("It is not prime")
                break

number = 30
check_prime(number)