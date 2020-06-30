#Write a Python function that accepts a string and calculate the number of
#upper case letters and lower case letters.

def check_cases(word):
    lowercase, uppercase = 0, 0
    for x in word:
        if x.isupper() == True:
            uppercase += 1
        elif x.islower() == True:
            lowercase += 1
    print("Uppercase : ", uppercase)
    print("Lowercase: ", lowercase)
        

word = "The quick Brown Fox"
check_cases(word) 