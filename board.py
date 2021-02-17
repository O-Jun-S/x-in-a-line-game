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
        print("    " + "   ".join(map(lambda num: str(num), range(self.width))))
        self.print_partition()
        for y in range(self.height):
            row = f"{y} |"
            for x in range(self.width):
                row += " "
                row += self.board_list[y][x]
                row += " |"
            print(row.strip())
            self.print_partition()

    def print_partition(self):
        print("-----" * self.width)

    def check_win(self):
        """check whether person who has the now turn is win."""
        return self.are_marks_in_a_row() or self.are_marks_in_a_column()

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

    def are_marks_in_a_row(self):
        for y in range(self.height):
            x_mark_count = 0
            for x in range(self.width):
                if self.board_list[y][x] == self.turn:
                    x_mark_count += 1

            if x_mark_count == self.width:
                return True
        return False

    def are_marks_in_a_column(self):
        for x in range(self.width):
            y_mark_count = 0
            for y in range(self.height):
                if self.board_list[y][x] == self.turn:
                    y_mark_count += 1
                    if y_mark_count == self.height:
                        return True
        return False
