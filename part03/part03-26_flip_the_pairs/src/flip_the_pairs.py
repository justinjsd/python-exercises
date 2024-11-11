# Write your solution here

num = int(input("Please type in a number: "))

n = 0

while n < num:
    n += 2
    if n > num:
        print(n-1)
    else:
        print(n)
        print(n-1)