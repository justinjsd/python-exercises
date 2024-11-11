# Write your solution here

string = input("Please type in a string: ")

n = 1
length = len(string)

while n <= length:
    print(string[:n])
    n += 1