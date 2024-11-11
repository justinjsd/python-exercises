# Write your solution here
def spruce(n):
    a = 1
    b = a
    itr = n
    sp = n - 1
    print("a spruce!")
    while itr >= 0:
        while a <= itr:
            print(" "*(n-1), end="")
            print("*"*b)
            b += 2
            a += 1
            n -= 1
        itr -= 1
    print(" "*sp, end="")
    print("*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)