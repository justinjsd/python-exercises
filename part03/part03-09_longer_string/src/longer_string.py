# Write your solution here

str1 = input("Please type in string 1: ")
str2 = input("Please type in string 2: ")

len1 = len(str1)
len2 = len(str2)

if len1 > len2:
    print(f"{str1} is longer")
elif len1 < len2:
    print(f"{str2} is longer")
else:
    print(f"The strings are equally long")
