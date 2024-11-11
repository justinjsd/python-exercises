# Write your solution here
import re

def change_case(orig_string: str):
    swapped_string = orig_string.swapcase()
    return swapped_string

def split_in_half(orig_string: str):
    length = int(len(orig_string))
    half_point = int(length/2)
    first_half = orig_string[:half_point]
    second_half = orig_string[half_point:]
    tuple = (first_half, second_half)
    return tuple

def remove_special_characters(orig_string: str):
    cleaned_string = re.sub(r'[^A-Za-z0-9 ]', '', orig_string)
    return cleaned_string

if __name__ == "__main__":
    change_case("Justin")
    split_in_half("Justint")
    remove_special_characters("Just*int")