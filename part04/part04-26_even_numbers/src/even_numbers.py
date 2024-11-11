# Write your solution here

def even_numbers(l1: list):
    l2 = []
    for elem in l1:
        if elem % 2 == 0:
            l2.append(elem)
    return l2

if __name__ == "__main__":
    my_list = [1, -1, 2, -2, 3, -3]
    new_list = even_numbers(my_list)
    print(f"original", my_list)
    print(f"new", new_list)
                           