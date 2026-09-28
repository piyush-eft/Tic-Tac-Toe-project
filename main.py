import numpy as np

SYMBOLS = {0: " ", 1: "X", -1: "O"}


def print_board(b):
    for r in range(3):
        print(" " + " | ".join(SYMBOLS[val] for val in b[r]))
        if r < 2:
            print("---+---+---")
    print()


def check_winner(b):
    # Every line's sum: 3 rows, 3 columns, 2 diagonals
    lines = list(b.sum(axis=1)) + list(b.sum(axis=0)) + [np.trace(b), np.trace(np.fliplr(b))]

    if 3 in lines:
        return "X"
    if -3 in lines:
        return "O"
    if not (b == 0).any():
        return "DRAW"
    return None


def main():
    board = np.zeros((3, 3), dtype=int)
    current = 1  # 1 = X, -1 = O

    print("Welcome to the tic tac toe game")
    print_board(board)

    while True:
        player = "X" if current == 1 else "O"

        try:
            row = int(input(f"{player} - Enter row (0,1,2): "))
            col = int(input(f"{player} - Enter column (0,1,2): "))
        except ValueError:
            print("Please enter numbers only.\n")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be between 0 and 2.\n")
            continue

        if board[row, col] != 0:
            print("Cell is already taken.\n")
            continue

        board[row, col] = current
        print_board(board)

        result = check_winner(board)
        if result == "DRAW":
            print("WOW! It's a draw")
            break
        if result is not None:
            print(result, "wins")
            break

        current = -current


if __name__ == "__main__":
    main()