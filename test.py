import unittest
from board import Board


class MyTestCase(unittest.TestCase):
    def test_board(self):
        board = Board(5, 5)
        self.assertEqual(
            board.board_list,
            [
                ["-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-"],
            ]
        )


if __name__ == '__main__':
    unittest.main()
