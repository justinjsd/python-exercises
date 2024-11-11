# Write your solution here

def longest(strings: list):
    max = 0
    max_string = ""
    for string in strings:
        if len(string) > max:
            max = len(string)
            max_string = string
    return max_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))