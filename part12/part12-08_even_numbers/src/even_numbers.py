# Write your solution here

def even_numbers(num: int, end: int):
    while num <= end:
        yield num
        num += 2

if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)