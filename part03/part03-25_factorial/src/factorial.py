# Write your solution here

number = 1

while number > 0:
    a = 1
    b = 1
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    while b <= number:
        a *= b
        b += 1

    print(f"The factorial of the number {number} is {a}")
print(f"Thanks and bye!")