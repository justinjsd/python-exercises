# Write your solution here

new_list = [] 
i = 0

while True:
    print(f"The list is now {new_list}")
    drx = input("a(d)d, (r)emove or e(x)it: ")
    if drx == 'x':
        print("Bye!")
        break
    elif drx == 'd':
        new_list.insert(i,i+1)
        i += 1
    elif drx == 'r':
        new_list.pop(len(new_list)-1)
        i -= 1
    else:
        continue
