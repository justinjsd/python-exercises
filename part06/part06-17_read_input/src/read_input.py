# Write your solution here

def read_input(string, x, y):
    while True:
        try:
            num = int(input(string))
            if num > x and num <= y:
                return num
        except ValueError:
            pass
        print(f"You must type in an integer between {x} and {y}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)