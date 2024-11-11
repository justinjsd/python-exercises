# Write your solution here

def formatted(my_list):
    new_list = []
    for elem in my_list:
        new_list.append(f"{elem:.2f}")
    return new_list

if __name__ == "__main__":
    new_list = formatted([1.234, 0.3333, 0.11111, 3.446])
    print(new_list)