# Write your solution here

from string import *

def separate_characters(my_string: str):
    parts0 = ""
    parts1 = ""
    parts2 = ""
    parts = ()
    for char in my_string:
        if char in ascii_letters:
            parts0 = f"{parts0}{char}"
        elif char in punctuation:
            parts1 = f"{parts1}{char}"
        else:
            parts2 = f"{parts2}{char}"
    parts = (parts0, parts1, parts2)
    return parts

if __name__ == "__main__":
    parts = separate_characters("a. s, d: f; g* ")
    print(parts)
