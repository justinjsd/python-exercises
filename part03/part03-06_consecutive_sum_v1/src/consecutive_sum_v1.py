# Write your solution here

limit = int(input("Limit: "))

num = 1
counter = 1 

while num < limit:
    counter += 1
    num += counter

print(num)