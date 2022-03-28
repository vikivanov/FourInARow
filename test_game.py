import pytest
import numpy as np
from config import ROWS, COLS
from game import check_diagonal_down, check_diagonal_up, check_horizontal, \
    check_valid_location, check_vertical, get_row_index, verify_input


@pytest.fixture
def board():
    return np.zeros((ROWS, COLS))


def test_verify_input():
    assert verify_input(-1) == False
    assert verify_input(1) == True
    assert verify_input(5) == True
    assert verify_input(7) == True
    assert verify_input(8) == False
    assert verify_input('a') == False
    assert verify_input('') == False


def test_check_valid_location(board):
    assert check_valid_location(board, 2) == True
    for r in range(ROWS):
        board[r][2] = 1
    assert check_valid_location(board, 2) == False
    assert check_valid_location(board, 5) == True


def test_get_row_index(board):
    assert get_row_index(board, 4) == 5
    for r in range(ROWS-1, 0, -1):
        board[r][4] = 2
    assert get_row_index(board, 4) == 0
    for r in range(ROWS-1, 2, -1):
        board[r][3] = 1
    assert get_row_index(board, 3) == 2
    board[5][0] = 1
    assert get_row_index(board, 0) == 4


def test_check_horizontal(board):
    assert check_horizontal(board, 1) == False
    for c in range(4):
        board[1][c] = 2
    assert check_horizontal(board, 2) == True
    for c in range(2, 6):
        board[3][c] = 1
    assert check_horizontal(board, 1) == True
    for c in range(3, 7):
        board[5][c] = 3
    assert check_horizontal(board, 3) == True
    assert check_horizontal(board, 4) == False


def test_check_vertical(board):
    assert check_vertical(board, 1) == False
    for r in range(4):
        board[r][0] = 2
    assert check_vertical(board, 2) == True
    for r in range(2, 6):
        board[r][4] = 1
    assert check_vertical(board, 1) == True
    for r in range(1, 5):
        board[r][6] = 3
    assert check_vertical(board, 3) == True
    assert check_vertical(board, 4) == False


def test_check_diagonal_down(board):
    assert check_diagonal_down(board, 1) == False
    board[2][0] = 1
    board[3][1] = 1
    board[4][2] = 1
    board[5][3] = 1
    assert check_diagonal_down(board, 1) == True
    board[0][0] = 2
    board[1][1] = 2
    board[2][2] = 2
    board[3][3] = 2
    assert check_diagonal_down(board, 2) == True
    board[2][3] = 3
    board[3][4] = 3
    board[4][5] = 3
    board[5][6] = 3
    assert check_diagonal_down(board, 3) == True
    assert check_diagonal_down(board, 4) == False


def test_check_diagonal_up(board):
    assert check_diagonal_up(board, 1) == False
    board[3][0] = 1
    board[2][1] = 1
    board[1][2] = 1
    board[0][3] = 1
    assert check_diagonal_up(board, 1) == True
    board[5][2] = 2
    board[4][3] = 2
    board[3][4] = 2
    board[2][5] = 2
    assert check_diagonal_up(board, 2) == True
    board[2][3] = 3
    board[3][4] = 3
    board[4][5] = 3
    board[5][6] = 3
    assert check_diagonal_up(board, 3) == False
    assert check_diagonal_up(board, 4) == False
