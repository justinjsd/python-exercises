# Write your solution here

# newlist = []

# items = int(input("How many items: "))
# n = 1

# while n <= items:
#     if n == -1:
#         break
#     if n <= 0 or n >= len(list):
#         print("Index is outside of the range of the list")
#         continue
#     newitem = int(input(f"Item {n}: "))
#     n += 1
#     newlist.append(newitem)

# print(newlist)

numbers = int(input("How many items: "))
list = []
 
while len(list) < numbers:
    number = int(input(f"Item {len(list) + 1}: "))
    list.append(number)
 
print(list)
 
