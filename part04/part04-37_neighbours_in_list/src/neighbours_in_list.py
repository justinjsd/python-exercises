# Write your solution here

def longest_series_of_neighbours(my_list: list):
    new_list = []
    i = 0
    size = 1
    while i < len(my_list):
        if i + 1 == len(my_list):
            break
        elif abs(my_list[i+1] - my_list[i]) == 1:
            size += 1
            new_list.append(size)
        else:
            size = 1
            i += 1
            continue
        i += 1
    return max(new_list) 

if __name__ == "__main__":
    print(longest_series_of_neighbours([0, 2, 4, 5, 6, 7, 10, 11, 12, 100, 101]))