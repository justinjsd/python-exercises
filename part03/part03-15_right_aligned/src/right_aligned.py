# Write your solution here

string = input("Please type in a string: ")

width = 20 - len(string)

starstring = "*"*width

print(f"{starstring}{string}")

