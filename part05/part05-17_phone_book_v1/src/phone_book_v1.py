# Write your solution here

def search(phone_book, name):
    if name in phone_book:
        for n in phone_book[name]:
            print(n)
    else:
        print("no number")

def add(phone_book, name, number):
    if name not in phone_book:
        phone_book[name] = []
    phone_book[name].append(number)
    print("ok!")

# Tester
phone_book = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 1:
        name = input("name: ")
        search(phone_book, name)
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        add(phone_book, name, number)
    else:
        print("quitting...")
        break