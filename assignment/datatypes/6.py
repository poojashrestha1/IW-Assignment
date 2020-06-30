#Write a Python program to find the first appearance of the substring 'not' and'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#substring with 'good'. Return the resulting string.


def check(string):
    split = string.split()
    index_not = string.find('not')
    #print(index_not)
    index_poor = string.find('poor')
    #print(index_poor)

    if 'not' in string:
        if 'poor' in string:
            if index_not < index_poor:
                new_string =  string[:index_not]
                print(new_string + 'good')

            else:
                print(string)
        else:
            print(string)
    else:
        print(string)

check("It is not that poor")
check("It is poor")
check("It is not poor")


