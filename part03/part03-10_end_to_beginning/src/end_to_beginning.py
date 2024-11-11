# Write your solution here

string = input("Please type in a string: ")

length = len(string)

while length > 0:
    print(string[length-1])
    length -= 1