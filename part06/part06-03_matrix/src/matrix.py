# write your solution here

def read_file(matrix_file):
    number_list = []
    with open(matrix_file) as matrix:
        for numbers in matrix:
            numbers = numbers.replace("\n", "")
            number = numbers.split(",")
            for n in number:
                number_list.append(int(n))
    return number_list

def read_file_row(matrix_file):
    row_sum = 0
    row_sum_list = []
    with open(matrix_file) as matrix:
        for numbers in matrix:
            numbers = numbers.replace("\n", "")
            number = numbers.split(",")
            for n in number:
                row_sum += int(n)
            row_sum_list.append(row_sum)
            row_sum = 0
    return row_sum_list

def matrix_sum():
    list = read_file("matrix.txt")
    mat_sum = sum(list)
    return mat_sum

def matrix_max():
    list = read_file("matrix.txt")
    mat_sum = max(list)
    return mat_sum

def row_sums():
    list = read_file_row("matrix.txt")