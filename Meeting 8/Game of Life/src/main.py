from conway_board import ConwayBoard


def choose_alive_cells(height, width):
    """
    Function to choose the alive cells
    :return: chosen alive cells
    """
    alive_cells = set()
    # Keep asking for alive cells as long as the user didn't enter 0 or didn't choose all cells
    while True:
        try:
            if len(alive_cells) == width * height:
                print('All cells are alive!')
                break
            # Choose row and column
            chosen_alive_cell_row = int(input(f'Choose an alive cell row (1 to {height} and 0 to exit): '))
            chosen_alive_cell_column = int(
                input(f'Choose an alive cell column (1 to {width} and 0 to exit): '))
            if chosen_alive_cell_row == 0 or chosen_alive_cell_column == 0:
                break
            if chosen_alive_cell_row < 1 or chosen_alive_cell_row > height:
                raise ValueError
            if chosen_alive_cell_column < 1 or chosen_alive_cell_column > width:
                raise ValueError

            alive_cells.add((chosen_alive_cell_row - 1, chosen_alive_cell_column - 1))
            print()
        except ValueError:
            print('Invalid cell')

    return alive_cells


def choose_number_of_rounds():
    """
    This function returns the number of rounds that the game will run based on user choice
    :return: the number of rounds that the game will run
    """
    while True:
        try:
            number_of_rounds = int(input('Enter the number of rounds you would like to simulate: '))
            # Don't allow less than 1 round
            if number_of_rounds < 1:
                raise Exception
            break
        except ValueError:
            print('Invalid input')
        except Exception:
            print('Please enter a proper number of rounds!')

    return number_of_rounds


def main():
    height = 8
    width = 8

    board = ConwayBoard(height=height, width=width)

    print('\nPlease choose the alive cells\n')
    chosen_alive_cells = choose_alive_cells(height=height, width=width)
    board.create_board(chosen_alive_cells=chosen_alive_cells)

    print()
    number_of_rounds = choose_number_of_rounds()

    board.play_game(number_of_rounds=number_of_rounds)
    board.show_results()


if __name__ == '__main__':
    main()
