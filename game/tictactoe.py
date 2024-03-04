from game.cellType import CellType
from game.invalid_move_exception import InvalidMoveException
from game.invalid_position_exception import InvalidPositionException


class TicTacToe:
    def __init__(self):
        self.board = [[CellType.EMPTY] * 3 for _ in range(3)]
        self.player = CellType.X

    def display_board(self):
        formatted_board = ""
        for column in self.board:
            formatted_board += "  ".join(str(row.name) for row in column) + "\n"
        print(formatted_board)
        return formatted_board

    @staticmethod
    def is_valid_move(move):
        if 1 <= move <= 9:
            return True
        raise InvalidMoveException("Move should be 1-9")

    def make_move(self, move):
        if self.is_valid_move(move):
            row = (move // 3) - 1 if move % 3 == 0 else move // 3
            if move % 3 == 0:
                column = 2
            else:
                column = (move % 3) - 1
            self.is_position_empty(row, column)
            self.board[row][column] = self.player
            self.player = CellType.O if self.player == CellType.X else CellType.X
            return True
        return False

    def is_position_empty(self, row, column):
        if self.board[row][column] != CellType.EMPTY:
            raise InvalidPositionException("The position is already occupied")

    def check_win(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != CellType.EMPTY:
                return True

        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != CellType.EMPTY:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != CellType.EMPTY:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != CellType.EMPTY:
            return True

        return False

    def check_tie(self):
        return all(cell != CellType.EMPTY for row in self.board for cell in row)

    def currentPlayer(self):
        return self.player
