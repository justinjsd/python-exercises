# write your solution here

def largest():
    max = 0
    with open("numbers.txt") as new_file:
        for line in new_file:
            if int(line) > max:
                max = int(line)
    return max

if __name__ == "__main__":
    print(largest())