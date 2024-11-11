# Write your solution here

num = int(input("Please type in a number: "))

n = 1

while n <= num:
    if n == num:
        print(n)
        break
    else:
        print(n)
        print(num)
        n += 1
        num -= 1