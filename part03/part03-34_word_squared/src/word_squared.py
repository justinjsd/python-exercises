# Write your solution here
def squared(s, n):
    a = 0
    c = 0
    while a < n:
        b = 0
        while b < n:
            print(s[c], end="")
            b += 1
            c += 1
            if c == len(s):
                c = 0
        print("\n")
        a += 1

# Testing the function
if __name__ == "__main__":
    s = input("Enter a string: ")
    n = int(input("Enter a number: "))
    squared(s, n)