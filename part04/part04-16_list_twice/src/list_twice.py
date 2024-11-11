# Write your solution here

l = []

while True:
    new_item = int(input("New item: "))
    if new_item == 0:
        print("Bye!")
        break
    l.append(new_item)
    print(f"The list now: {l}")
    print(f"The list in order: {sorted(l)}")
