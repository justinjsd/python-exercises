# Write your solution here
def chessboard(n):
    a = 0
    while a < n:
        b = 0
        while b < n:
            if a % 2 == 0:
                if b % 2 == 0:
                    print(1, end="")
                else:
                    print(0, end="")
            else:
                if b % 2 == 0:
                    print(0, end="")
                else:
                    print(1, end="")
            b += 1
        print("\n")
        a += 1

# Testing the function
if __name__ == "__main__":
    squares = int(input("Enter the number of chessboard squares: "))
    chessboard(squares)