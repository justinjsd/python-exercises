# Write your solution here

def print_sudoku(sudoku: list):
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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
 
    new_list[row_no][column_no] = number
    return new_list

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)