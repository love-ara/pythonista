from game.cellType import CellType
from game.invalid_move_exception import InvalidMoveException
from game.tictactoe import TicTacToe


class PlayTicTacToe:
    def __init__(self):
        self.board = [[CellType.EMPTY] * 3 for _ in range(3)]
        self.game = TicTacToe()

    def play(self):
        print("Let's play the game!")
        self.game.display_board()
        while not self.game.check_win() and not self.game.check_tie():
            try:
                print("It's your turn Player ", self.game.player.name)
                move = int(input("Enter your move (1-9): "))
                if not self.game.make_move(move):
                    raise InvalidMoveException("Invalid move")
            except Exception as e:
                print(e)
            finally:
                self.game.display_board()

        if self.game.check_win():
            winner = CellType.O if self.game.currentPlayer() == CellType.X else CellType.X
            print(f"Player {winner.name} Wins!")
        else:
            print("It's a draw!")


main: PlayTicTacToe = PlayTicTacToe()
main.play()
