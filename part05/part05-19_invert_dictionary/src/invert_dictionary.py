# Write your solution here

def invert(dictionary: dict):
    new_dict = {}
    for keys in dictionary:
        new_key = dictionary[keys]
        new_dict[new_key] = keys
    
    dictionary.clear()
    dictionary.update(new_dict)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)