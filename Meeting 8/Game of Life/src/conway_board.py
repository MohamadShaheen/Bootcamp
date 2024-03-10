import numpy as np
import tkinter as tk


class ConwayBoard:
    def __init__(self, height, width):
        """
        Initialize the game of life board with width and height
        :param height: the height of the board
        :param width: the width of the board
        """
        self.height = height
        self.width = width
        self.board = np.zeros((height, width), dtype=int)

        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")

        # Create a frame to hold the board elements
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Initialize the board
        self.initialize_board()

    def initialize_board(self):
        """
        Function to initialize the board GUI
        """
        # Display the initial board elements in a grid
        for i in range(self.height):
            for j in range(self.width):
                cell_label = tk.Label(self.frame, text='', width=2, height=1, relief="solid")
                cell_label.grid(row=i, column=j, padx=1, pady=1)

    def update_board(self):
        """
        Function to update the board with new values and to print logs accordingly
        """
        print("Current board state:")
        for i in range(self.height):
            row_string = ''
            for j in range(self.width):
                cell_label = self.frame.grid_slaves(row=i, column=j)[0]
                if self.board[i][j] == 1:
                    row_string += 'X\t'
                    cell_label.config(bg='black')
                else:
                    row_string += '- \t'
                    cell_label.config(bg='white')
            print(row_string)
        print()

    def create_board(self, chosen_alive_cells):
        """
        Function to create the board based on the chosen alive cells
        :param chosen_alive_cells: represents the alive cells chosen by the user
        """
        for row, column in chosen_alive_cells:
            self.board[row][column] = 1

    def _get_alive_neighbors(self, cell_row, cell_column):
        """
        Function to get the alive neighbors of the given cell
        :param cell_row: the given cell row in the board
        :param cell_column: the given cell column in the board
        :return: the number of alive neighbors of the given cell
        """
        alive_neighbors = 0
        offsets = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)]

        for offset in offsets:
            neighbor_row = cell_row + offset[0]
            neighbor_column = cell_column + offset[1]

            # Wrap around if neighbor is out of bounds
            neighbor_row = neighbor_row % self.height
            neighbor_column = neighbor_column % self.width

            if self.board[neighbor_row][neighbor_column] == 1:
                alive_neighbors += 1

        return alive_neighbors

    def play_game(self, number_of_rounds):
        """
        Function to simulate a game of life on the board for a given number of rounds
        :param number_of_rounds: the number of rounds that will be simulated
        """
        # Create a copy of the original board to prevent the effect of updated cells
        temp_board = self.board.copy()
        for i in range(number_of_rounds):
            # Print round number
            print(f'Round {i + 1}')
            for row in range(self.height):
                for column in range(self.width):
                    number_of_alive_neighbors = self._get_alive_neighbors(cell_row=row, cell_column=column)

                    if number_of_alive_neighbors < 2 or number_of_alive_neighbors > 3:
                        temp_board[row][column] = 0
                    elif number_of_alive_neighbors == 3:
                        temp_board[row][column] = 1

            self.board = temp_board.copy()
            self.update_board()
            self.root.update()
            self.root.after(3000)  # Delay for 3 seconds

    def show_results(self):
        self.root.mainloop()
