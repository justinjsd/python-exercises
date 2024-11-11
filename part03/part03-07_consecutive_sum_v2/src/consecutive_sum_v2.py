# Write your solution here

limit = int(input("Limit: "))

num = 1
counter = 1 

sentence = "The consecutive sum: 1"

while num < limit:
    counter += 1
    num += counter
    sentence += f" + {counter}"

print(f"{sentence} = {num}")