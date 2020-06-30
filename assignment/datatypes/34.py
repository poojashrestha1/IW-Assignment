#Write a Python script to merge two Python dictionaries.

dict1 = {"name": "Insight", "place": "Online"}
dict2 = {"class": "Python", "day": "Sunday"}

print("Dictionary 1 =", dict1)
print("Dictionary 2 =", dict2)

dict1.update(dict2)


print("The merged dictionary:", dict1)