# Write your solution here

def histogram(string: str):
    my_dict = {}
    for char in string:
        my_dict[char] = string.count(char)

    for char in my_dict:    
        print(f"{char} "+"*"*my_dict[char])

if __name__ == "__main__":
    histogram("hehe")