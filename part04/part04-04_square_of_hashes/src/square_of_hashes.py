# Copy here code of line function from previous exercise
# Copy here code of line function from previous exercise
def line(size):
    itr = 0
    while itr < size:
        print("#"*size)
        itr += 1

def square_of_hashes(size):
    # You should call function line here with proper parameters
    line(size)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
