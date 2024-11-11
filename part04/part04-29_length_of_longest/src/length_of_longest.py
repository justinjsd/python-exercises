# Write your solution here

def length_of_shortest(l: list):
    length = 0
    for elem in l:
        if len(elem) < length:
            length = len(elem)
    return length
 
if __name__ == "__main__":
    print(length_of_shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))