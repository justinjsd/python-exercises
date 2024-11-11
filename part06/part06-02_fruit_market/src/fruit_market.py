# write your solution here

def read_fruits():
    fruit_dict = {}
    with open("fruits.csv") as fruits:
        for fruit in fruits:
            fruit = fruit.replace("\n", "")
            f = fruit.split(";")
            fruit_dict[f[0]] = float(f[1])
    return fruit_dict

if __name__ == "__main__":
    print(read_fruits())