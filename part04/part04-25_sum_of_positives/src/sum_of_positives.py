# Write your solution here

def sum_of_positives(l: list):
    sum = 0
    for i in l:
        if i > 0:
            sum += i
    return sum

if __name__ == "__main__":
    sum = sum_of_positives([1, -1, 2, -2, 3, -3])
    print(sum)
                           