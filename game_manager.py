import sys
from board import Board


BOARD_WIDTH = 5
BOARD_HEIGHT = 5


class GameManager:
    def __init__(self):
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT)

    def turn_manage(self):
        """Manage a turn.."""
        self.turn_routine()
        if self.board.check_win():
            print(f"{self.board.turn} WON !")
            self.board.print_board()
            sys.exit(0)

        if self.board.turn == "o":
            self.board.turn = "x"

        elif self.board.turn == "x":
            self.board.turn = "o"

    def turn_routine(self):
        """Doing that is done once a turn."""
        self.board.print_board()
        self.board.put_mark_prompt()
