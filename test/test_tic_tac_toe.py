import unittest

from game.cellType import CellType
from game.invalid_move_exception import InvalidMoveException
from game.invalid_position_exception import InvalidPositionException
from game.tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_board_displays_empty_at_start_of_game(self):
        expected_board = """EMPTY  EMPTY  EMPTY
EMPTY  EMPTY  EMPTY
EMPTY  EMPTY  EMPTY
"""
        self.assertEqual(expected_board, self.game.display_board())

    def test_that_the_first_player_plays_typeX(self):
        self.assertEqual(self.game.player, self.game.currentPlayer())

    def test_that_the_second_player_plays_typeO(self):
        player = CellType.X
        self.assertEqual(player, self.game.currentPlayer())
        self.game.make_move(2)
        player2 = CellType.O
        self.assertEqual(player2, self.game.currentPlayer())

    def test_player_can_make_move(self):
        self.assertTrue(self.game.make_move(3))

    def test_player_plays_a_valid_move(self):
        self.game.make_move(2)
        self.assertTrue(self.game.is_valid_move(2))

    def test_that_invalid_move_throws_exception(self):
        self.game.make_move(2)
        with self.assertRaises(InvalidMoveException):
            self.game.make_move(10)

    def test_that_invalid_position_throws_exception(self):
        self.game.make_move(2)
        with self.assertRaises(InvalidPositionException):
            self.game.make_move(2)

    def test_that_a_player_wins_the_game(self):
        self.game.make_move(2)
        self.game.make_move(1)
        self.game.make_move(4)
        self.game.make_move(5)
        self.game.make_move(8)
        self.game.make_move(9)
        self.assertTrue(self.game.check_win())

    def test_that_the_players_can_have_a_tie(self):
        self.game.make_move(5)
        self.game.make_move(9)
        self.game.make_move(3)
        self.game.make_move(7)
        self.game.make_move(8)
        self.game.make_move(2)
        self.game.make_move(4)
        self.game.make_move(6)
        self.game.make_move(1)
        self.assertTrue(self.game.check_tie())
