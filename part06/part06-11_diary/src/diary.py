# Write your solution here

def add_to_file(file):
    entry = input("Diary entry: ")
    with open(file, "a") as file:
        file.write(f"{entry}\n")

def read_file(file):
    with open(file) as file:
        for entries in file:
            print(entries.rstrip())

file = "diary.txt"
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    func = int(input("Function: "))
    if func == 1:
        add_to_file(file)
    elif func == 2:
        read_file(file)
    else:
        print("Bye now!")
        break