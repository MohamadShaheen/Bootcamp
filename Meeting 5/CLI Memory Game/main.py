import random
import numpy as np


def print_board(board):
    for row in board:
        for cell in row:
            print(f'{cell}\t', end='')

        print()


def print_board_specific_cells(board, cells):
    counter = 0
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if (i, j) not in cells:
                print(f'-\t', end='')
            else:
                print(f'{board[i][j]}\t', end='')
                counter += 1

        print()

    return counter


def main():
    pairs = random.sample(range(10, 28), 18) * 2
    indices = random.sample(range(36), 36)
    board = np.array([pairs[i] for i in indices]).reshape(6, 6)
    cells = []
    print_board(board)
    print()

    counter = 0

    while counter != 36:
        # while True:
        #     try:
        #         row = int(input('Guess a row (1 - 6): '))
        #         if not (1 <= row <= 6):
        #             raise ValueError
        #         break
        #     except ValueError:
        #         print('Please enter a valid integer')
        #
        # while True:
        #     try:
        #         column = int(input('Guess a column (1 - 6): '))
        #         if not (1 <= column <= 6):
        #             raise ValueError
        #         break
        #     except ValueError:
        #         print('Please enter a valid integer')

        first_row = random.randint(1, 6)
        first_column = random.randint(1, 6)
        cells.append((first_row - 1, first_column - 1))
        print_board_specific_cells(board, cells)
        first_guess = board[first_row - 1][first_column - 1]

        print()

        second_row = random.randint(1, 6)
        second_column = random.randint(1, 6)
        cells.append((second_row - 1, second_column - 1))
        counter = print_board_specific_cells(board, cells)
        second_guess = board[second_row - 1][second_column - 1]

        print()

        if first_row == second_row and first_column == second_column:
            cells = cells[:-2]
        else:
            if not (first_guess == second_guess):
                cells = cells[:-2]


if __name__ == '__main__':
    main()
