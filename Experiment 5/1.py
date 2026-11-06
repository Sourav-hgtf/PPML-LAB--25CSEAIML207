dict1 = dict(eval(input("Enter a dictionary values: ")))
print(dict1)

dict2 = dict(eval(input("Enter a dictionary values: ")))
print(dict2)

dict1.update(dict2)

print("After merging the dictionaries:")
print(dict1)