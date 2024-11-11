# Write your solution here

def times_ten(start_index: int, end_index: int):
    dick = {}
    while start_index <= end_index:
        dick[start_index] = start_index * 10
        start_index += 1
    return dick

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)    