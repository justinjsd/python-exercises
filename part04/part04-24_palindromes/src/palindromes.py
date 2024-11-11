# Write your solution here
def palindromes(s):
    if s == s[::-1]:
        return True
    else:
        return False

def main():
    while True:
        s = input("Please type in a palindrome: ")

        if palindromes(s):
            print(f"{s} is a palindrome!")
            break

        else:
            print("that wasn't a palindrome")
main()