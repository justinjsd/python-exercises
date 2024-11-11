# Write your solution here

num = int(input("Please type in a number: "))

a = 1
b = 1

while a <= num:
    while b <= num:
        print(f"{a} x {b} = {a*b}")
        b += 1
    b = 1
    a += 1