# Write your solution here

def prime_numbers():
    number = 2
    while True:
        for a in range(2,number):
            if number % a ==0:
                break
        else:
            yield number
        number += 1

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))