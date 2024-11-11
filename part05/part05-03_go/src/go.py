# Write your solution here

def who_won(game_board: list):
    counter_1 = 0
    counter_2 = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                counter_1 += 1
            elif game_board[i][j] == 2:
                counter_2 += 1
    if counter_1 > counter_2:
        return 1
    elif counter_2 > counter_1:
        return 2
    else:
        return 0
    
if __name__ == "__main__":
    game_board = [
    [1, 0, 0, 0, 8, 0, 1, 0, 0],
    [2, 0, 0, 2, 2, 0, 1, 0, 0],
    [0, 2, 0, 1, 0, 0, 0, 0, 1],
    [2, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 3, 0, 2, 2, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 2, 0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(who_won(game_board))