# Write your solution here

def shortest(l: list):
    length = 1000
    shorty = ""
    for elem in l:
        if len(elem) <= length:
            length = len(elem)
            shorty = elem
    return shorty
 
if __name__ == "__main__":
    print(shortest(['Alan', 'Susan', 'Seymour', 'Kim', 'Susan']))