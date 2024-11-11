# Write your solution here

def print_many_times(string, num):
    n = 0
    while n < num:
        print(string)
        n += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)