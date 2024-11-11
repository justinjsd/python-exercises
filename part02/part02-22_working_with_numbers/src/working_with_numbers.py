# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

add = 0
counter = 0
pos = 0
neg = 0

while True:
    num = int(input("Number: "))
    if num == 0:
        break
    else:
        counter += 1
        add += num
        mean = add/counter
        if num > 0:
            pos += 1
        else:
            neg += 1

print(f"Numbers typed in {counter}")
print(f"The sum of the numbers is {add}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")