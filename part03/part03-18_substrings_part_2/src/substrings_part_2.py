# Write your solution here

string = input("Please type in a string: ")

n = len(string) - 1

while n >= 0:
    print(string[n:])
    n -= 1