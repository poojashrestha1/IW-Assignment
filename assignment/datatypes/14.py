#Write a Python function to create the HTML string with tags around the word(s).

def add_tags(tag, string):
    result = "<"+ tag + ">" + string + "</" + tag + ">"
    print(result)

add_tags("p","This is a paragraph")