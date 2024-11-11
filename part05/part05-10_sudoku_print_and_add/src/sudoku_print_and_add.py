# Write your solution here

def print_sudoku(sudoku: list):
    i = 0
    j = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                print("_ ", end = "")
                if j == 2 or j == 5:
                    print(" ", end = "")
            else:
                print(f"{sudoku[i][j]} ", end = "")
                if j == 2 or j == 5:
                    print(" ", end = "")
        if i == 2 or i == 5:
            print("\n")
        else:
            print()
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku  = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)