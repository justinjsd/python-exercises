# Copy here code of line function from previous exercise
def line(size):
    a = 1
    b = 1
    while a <= size:
        while b <= size:
            print("#"*b)
            b += 1
        a += 1

def triangle(size):
    # You should call function line here with proper parameters
    line(size)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
