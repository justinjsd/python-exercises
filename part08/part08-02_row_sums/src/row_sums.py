# Write your solution here

def row_sums(my_matrix: list):
    for list in my_matrix:
        list.append(sum(list))

if __name__ == "__main__":
    my_matrix = [[1,1],[2,2]]
    row_sums(my_matrix)
    print(my_matrix)