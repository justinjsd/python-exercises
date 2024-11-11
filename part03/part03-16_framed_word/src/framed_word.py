# Write your solution here

string = input("Word: ")

print("*"*30)

width = len(string)
start = int((30 - width)/2 - 1)

if width%2 == 0:
    print("*"+" "*start+string+" "*start+"*")
else:
    print("*"+" "*start+string+" "*(start+1)+"*")

print("*"*30)