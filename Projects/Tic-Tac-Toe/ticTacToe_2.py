""" Current State...
> It declares the winner (Partially) & The Game Ends (Partially).

> It only works for 3x3. Should it be the case? => No. 
    > Make it Dynamic...

> Every choice should be Immutable & No Input Validations
"""


class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def __str__(self):
        return self.name


class Board:
    def __init__(self, rows, cols):
        self.board = []
        self.rows = rows
        self.cols = cols
        self.create_board()

    def create_board(self):
        for row in range(self.rows):
            temp = []
            for col in range(self.cols):
                temp.append('-')

            self.board.append(temp)

    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.board[row][col], end=" ")
            print()

    def show_options(self):
        print("\nSelect a cell to put a marker:")
        cell_number = 0

        for row in range(self.rows):
            for col in range(self.cols):
                print(cell_number, end=" ")
                cell_number += 1
            print()
        print()

    def place_marker(self, cell_number, marker):
        row_num, col_num = None, None
        grid_pos = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if cell_number == grid_pos:
                    row_num = row
                    col_num = col

                grid_pos += 1

        self.board[row_num][col_num] = marker

    def has_consecutive_marker_on_rows(self):
        """
        X X -
        O - -
        - - -
    -----------------
        ROW -> 0
        COL -> 0
        """

        for row in range(self.rows):
            for col in range(self.cols):

                # if col == 1:
                #     col -= 1
                #     pass

                current_cell_value = self.board[row][col]
                next_cell_value = self.board[row][col + 1]
                last_cell_value = self.board[row][col + 2]

                if current_cell_value == next_cell_value and next_cell_value == last_cell_value and current_cell_value != '-':
                    return True
                else:
                    break

    def has_consecutive_marker_on_columns(self):
        for row in range(self.rows):
            for col in range(self.cols):

                # if col == 1:
                #     col -= 1
                #     pass

                current_cell_value = self.board[row][col]
                next_cell_value = self.board[row + 1][col]
                last_cell_value = self.board[row + 2][col]

                if current_cell_value == next_cell_value and next_cell_value == last_cell_value and current_cell_value != '-':
                    return True
                else:
                    break


class TicTacToe:
    def __init__(self, player_1, player_2, board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
        self.current_player = self.player_1
        self.status = 'ONGOING'

    def get_user_input(self):
        return int(input(f"{self.current_player} Choice: "))

    def play(self):
        self.board.display()
        self.board.show_options()

        cell_number = self.get_user_input()
        self.board.place_marker(
            cell_number,
            self.current_player.marker
        )

        if self.has_winner():
            self.end_game()
        else:
            self.swap_player()

        # if self.is_draw():
        #     pass
        #     return

    def has_winner(self):
        return self.board.has_consecutive_marker_on_rows() or self.board.has_consecutive_marker_on_columns() \
            #    or self.board.has_consecutive_marker_on_diagonal()

    def end_game(self):
        self.status = 'END'

    def declare_winner(self):
        print('won by ', self.current_player)

    def swap_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1


if __name__ == "__main__":
    first_player = Player(name="Player 1", marker="X")
    second_player = Player(name="Player 2", marker="O")

    tictactoe_board = Board(rows=3, cols=3)

    game = TicTacToe(
        player_1=first_player,
        player_2=second_player,
        board=tictactoe_board
    )

    while game.status == 'ONGOING':
        game.play()

    game.declare_winner()


class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def __str__(self):
        return self.name


class Board:
    def __init__(self, rows, cols):
        self.board = []
        self.rows = rows
        self.cols = cols
        self.create_board()

    def create_board(self):
        for row in range(self.rows):
            temp = []
            for col in range(self.cols):
                temp.append('-')

            self.board.append(temp)

    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.board[row][col], end=" ")
            print()

    def show_options(self):
        print("\nSelect a cell to put a marker:")
        cell_number = 0

        for row in range(self.rows):
            for col in range(self.cols):
                print(cell_number, end=" ")
                cell_number += 1
            print()
        print()

    def place_marker(self, cell_number, marker):
        row_num, col_num = None, None
        grid_pos = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if cell_number == grid_pos:
                    row_num = row
                    col_num = col

                grid_pos += 1

        self.board[row_num][col_num] = marker

    def has_consecutive_marker_on_rows(self):
        for row in range(self.rows):
            has_consecutive_marker = True
            prev_marker = self.board[row][0]

            if prev_marker == '-':
                continue

            for col in range(self.cols):
                current_cell_value = self.board[row][col]
                if current_cell_value != prev_marker or current_cell_value == '-':
                    has_consecutive_marker = False
                    break

            if has_consecutive_marker:
                return True

        return False

    def has_consecutive_marker_on_columns(self):
        for col in range(self.cols):
            has_consecutive_marker = True
            prev_marker = self.board[0][col]

            if prev_marker == '-':
                continue

            for row in range(self.rows):
                current_cell_value = self.board[row][col]

                if current_cell_value != prev_marker or current_cell_value == '-':
                    has_consecutive_marker = False
                    break

            if has_consecutive_marker:
                return True

        return False

    def has_consecutive_marker_on_diagonal(self):
        return self._has_consecutive_marker_on_first_diagonal() or self._has_consecutive_marker_on_second_diagonal()

    def _has_consecutive_marker_on_first_diagonal(self):
        prev_marker = self.board[0][0]

        for i in range(self.rows):
            diagonal_element = self.board[i][i]
            if prev_marker == '-' or diagonal_element != prev_marker:
                return False

        return True

    def _has_consecutive_marker_on_second_diagonal(self):
        last_element_index = self.rows - 1
        prev_marker = self.board[0][last_element_index]

        for i in range(last_element_index, -1, -1):
            diagonal_element = self.board[i][i]
            if prev_marker == '-' or diagonal_element != prev_marker:
                return False

        return True


class TicTacToe:
    def __init__(self, player_1, player_2, board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
        self.current_player = self.player_1
        self.status = 'ONGOING'

    def get_user_input(self):
        return int(input(f"{self.current_player} Choice: "))

    def play(self):
        self.board.display()
        self.board.show_options()

        cell_number = self.get_user_input()
        self.board.place_marker(
            cell_number,
            self.current_player.marker
        )

        if self.has_winner():
            self.end_game()
        else:
            self.swap_player()

        # if self.is_draw():
        #     pass
        #     return

    def has_winner(self):
        return self.board.has_consecutive_marker_on_rows() \
            or self.board.has_consecutive_marker_on_columns() \
            or self.board.has_consecutive_marker_on_diagonal()

    def end_game(self):
        self.status = 'END'

    def declare_winner(self):
        print('won by ', self.current_player)

    def swap_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1


if __name__ == "__main__":
    first_player = Player(name="Player 1", marker="X")
    second_player = Player(name="Player 2", marker="O")

    tictactoe_board = Board(rows=3, cols=3)

    game = TicTacToe(
        player_1=first_player,
        player_2=second_player,
        board=tictactoe_board
    )

    while game.status == 'ONGOING':
        game.play()

    game.declare_winner()
