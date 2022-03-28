import numpy as np
from config import ROWS, COLS


def initialize_game_board() -> np.ndarray:
    return np.zeros((ROWS, COLS))


def verify_input(input: str) -> bool:
    try:
        position = int(input)
        if not 1 <= position <= 7:
            print('Input out of range. Please enter a number between 1 and 7!')
            return False
        return True
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 7!')
        return False


def check_valid_location(board: np.ndarray, col: int) -> bool:
    return board[0][col] == 0


def get_row_index(board: np.ndarray, col: int) -> int:
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == 0:
            return r


def check_horizontal(board: np.ndarray, player: int) -> bool:
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == player and \
                    board[r][c+1] == player and \
                    board[r][c+2] == player and \
                    board[r][c+3] == player:
                return True
    return False


def check_vertical(board: np.ndarray, player: int) -> bool:
    for r in range(ROWS - 3):
        for c in range(COLS):
            if board[r][c] == player and \
                    board[r+1][c] == player and \
                    board[r+2][c] == player and \
                    board[r+3][c] == player:
                return True
    return False


def check_diagonal_down(board: np.ndarray, player: int) -> bool:
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if board[r][c] == player and \
                    board[r+1][c+1] == player and \
                    board[r+2][c+2] == player and \
                    board[r+3][c+3] == player:
                return True
    return False


def check_diagonal_up(board: np.ndarray, player: int) -> bool:
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if board[r][c] == player and \
                    board[r-1][c+1] == player and \
                    board[r-2][c+2] == player and \
                    board[r-3][c+3] == player:
                return True
    return False


def check_winner(board: np.ndarray, player: int) -> bool:
    return check_horizontal(board, player) or \
        check_vertical(board, player) or \
        check_diagonal_down(board, player) or \
        check_diagonal_up(board, player)


if __name__ == "__main__":
    board = initialize_game_board()
    game_over = False
    turn = 0
    while not game_over:
        print(board)
        player = 1 if turn % 2 == 0 else 2
        if player == 1:
            player_input = input('Player 1, pick column [1-7]! ')
        else:
            player_input = input('Player 2, pick column [1-7]! ')
        if not verify_input(player_input):
            continue
        col = int(player_input) - 1
        if not check_valid_location(board, col):
            print('Invalid column. Please pick another column!')
            continue
        row = get_row_index(board, col)
        board[row][col] = player
        turn += 1
        if check_winner(board, player):
            print(board)
            print(f'Player {player} wins!')
            game_over = True
