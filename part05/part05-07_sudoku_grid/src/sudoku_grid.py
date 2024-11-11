# Write your solution here
def row_correct(sudoku: list, row_no: int):
    new_list = []
    for i in range(0, 9):
        sudoku[row_no][i]
        if sudoku[row_no][i] > 0 and  sudoku[row_no][i] in new_list:
            return False
        else:
            new_list.append(sudoku[row_no][i])
        
    return True

def column_correct(sudoku : list, column_no: int):
    new_list = []
    for i in range(len(sudoku)): 
        for j in range(len(sudoku[i])): 
            if sudoku[i][column_no] > 0 and  sudoku[i][column_no] in new_list:
                return False
        else:
            new_list.append(sudoku[i][column_no])

    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list = []
    for row in range(row_no, row_no+3):
        for element in range(column_no, column_no+3):
            number = sudoku[row][element]
            if number > 0 and number in new_list:
                return False
            new_list.append(number)
 
    return True

def sudoku_grid_correct(sudoku: list):
    row_no = 0
    rc = True
    cc = True
    bc = True
    while row_no < 9:
        column_no = row_no
        rc = row_correct(sudoku, row_no)
        cc = column_correct(sudoku, column_no)
        if rc == False or cc == False:
            return False
        row_no += 1
    
    row_no = 0
    column_no = 0
    while row_no < 9:
        while column_no < 9:
            bc = block_correct(sudoku, row_no, column_no)
            if bc == False:
                return False
            row_no += 3
            column_no += 3
    return True

if __name__ == "__main__":

    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    is_correct = sudoku_grid_correct(sudoku)
    print(is_correct)