import unittest
from tic_tac_toe import (
    board,
    handle_turn,
    check_rows,
    check_columns,
    check_diagonals,
    check_if_tie,
    flip_player,
    current_player,
)

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Reset the board and global variables for each test
        global board, current_player
        board[:] = ["-"] * 9
        current_player = "X"

    def test_handle_turn(self):
        handle_turn("X")
        self.assertIn("X", board)
        self.assertNotIn("-", board[:1])  # Ensure board updated

    def test_check_rows(self):
        global board
        board[0] = board[1] = board[2] = "X"  # Simulate a win
        self.assertEqual(check_rows(), "X")

    def test_check_columns(self):
        global board
        board[0] = board[3] = board[6] = "O"  # Simulate a win
        self.assertEqual(check_columns(), "O")

    def test_check_diagonals(self):
        global board
        board[0] = board[4] = board[8] = "X"  # Simulate a win
        self.assertEqual(check_diagonals(), "X")

    def test_check_if_tie(self):
        global board
        # Fill the board without a winner
        board[:] = ["X", "O", "X", "X", "X", "O", "O", "X", "O"]
        self.assertFalse(check_if_tie())  # Returns False since it's a tie
        self.assertNotIn("-", board)

    def test_flip_player(self):
        global current_player
        flip_player()
        self.assertEqual(current_player, "O")
        flip_player()
        self.assertEqual(current_player, "X")

if __name__ == "__main__":
    unittest.main()
