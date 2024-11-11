# Copy here code of line function from previous exercise
def line(n, s):
    itr = 0
    while itr < n:
        while True:
            if len(s) == 0:
                print("*"*n)
            else:
                print(s[0]*n)
            break
        itr += 1

def square(size, character):
    # You should call function line here with proper parameters
    line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "#")