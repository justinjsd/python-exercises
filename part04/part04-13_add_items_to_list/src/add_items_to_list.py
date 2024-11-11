numbers = int(input("How many items: "))
list = []
 
while len(list) < numbers:
    number = int(input(f"Item {len(list) + 1}: "))
    list.append(number)
 
print(list)
 