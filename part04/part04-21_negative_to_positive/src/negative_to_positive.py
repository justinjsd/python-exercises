# Write your solution here

n = int(input("Please type in a positive integer: "))

for i in range(-n, n+1, 1):
    if i == 0:
        continue
    else:
        print(i)