#Write a Python program to add 'ing' at the end of a given string (length should
#be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
#string length of the given string is less than 3, leave it unchanged.


string = "abcdingdf"
ing = string[-3:]

if len(string)>3:
    if ing == 'ing':
        new_string = string.replace(ing, 'ly')
        print(new_string)
    else:
        new_string = string + 'ing'
        print(new_string)