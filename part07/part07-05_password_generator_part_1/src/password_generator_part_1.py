# Write your solution here
from string import *
from random import *


def generate_password(times: int):
    letters = ascii_lowercase
    letters_pool = sample(letters, times)
    return ''.join(letters_pool)

if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    times = int(input("Enter how many passwords you want to generate: "))
    for i in range(times):
        print(generate_password(length))