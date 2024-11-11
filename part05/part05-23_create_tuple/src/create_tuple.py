# Write your solution here

def create_tuple(x: int, y: int, z: int):
    minimum = min(x, y, z) 
    maxiumum = max(x, y, z) 
    add = x + y + z
    t1 = (minimum, maxiumum, add)
    return t1

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))