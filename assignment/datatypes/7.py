#Write a Python function that takes a list of words and returns the length of the longest one.


def longest(words):
    longest = 0
    for i in words:
        if len(i) > longest:
            longest = len(i)
    print(longest)

longest(['list', 'pooja', 'insight'])
