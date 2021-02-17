from prettytable import PrettyTable
from prettytable import PLAIN_COLUMNS


# style of printing the game-board.
STYLE = PLAIN_COLUMNS


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board_list = []
        self.create_board()
        self.turn = "o"

    def create_board(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append("-")
            self.board_list.append(row)

    def print_board(self):
        """print board using PrettyTable."""

        # create table.
        table = PrettyTable()
        table.set_style(STYLE)

        # add data about first row to the table.
        field_names = ["game"]
        field_names.extend(str(_int) for _int in range(self.height))
        table.field_names = field_names

        # add data about from second row to last row to the table.
        for y in range(self.height):
            row = [str(y)]
            row.extend(self.board_list[y])
            table.add_row(row)

        print(table.get_string())

    def check_win(self):
        """check whether person who has the now turn is win."""
        return self.same_marks_in_a_row() or self.same_marks_in_a_column()

    def put_mark(self, x, y):
        """put mark to the board according to the arguments."""
        self.board_list[y][x] = self.turn

    def put_mark_prompt(self):
        """get information from player about putting mark."""
        print(f"Now the turn is {self.turn}'s turn.")
        x = int(input(f"Which column do you want to put your mark ({self.turn})?: "))
        if x < 0 or x > self.width:
            print(f"Input value from 0 to {self.width}.")
            self.put_mark_prompt()

        y = int(input(f"Which row do you want to put your mark ({self.turn})?: "))
        if y < 0 or y > self.height:
            print(f"Input value from 0 to {self.height}.")
            self.put_mark_prompt()

        self.put_mark(x, y)

    def same_marks_in_a_row(self):
        """check if the same marks in a row"""
        for y in range(self.height):
            x_mark_count = 0
            for x in range(self.width):
                if self.board_list[y][x] == self.turn:
                    x_mark_count += 1

            if x_mark_count == self.width:
                return True
        return False

    def same_marks_in_a_column(self):
        """check if the same marks in a column"""
        for x in range(self.width):
            y_mark_count = 0
            for y in range(self.height):
                if self.board_list[y][x] == self.turn:
                    y_mark_count += 1
                    if y_mark_count == self.height:
                        return True
        return False


if __name__ == '__main__':
    board = Board(10, 10)
    board.print_board()
