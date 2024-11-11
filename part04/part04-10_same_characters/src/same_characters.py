# Write your solution here
def same_chars(char, a, b):
    if a >= len(char) or b >= len(char) or char[a] != char[b]:
        return False
    else:
        return True
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))