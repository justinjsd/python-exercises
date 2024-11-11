# Write your solution here
def line(n, s):
    while True:
        if len(s) == 0:
            print("*"*n)
        else:
            print(s[0]*n)
        break
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")