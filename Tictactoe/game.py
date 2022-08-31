
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # use single list to rep 3x3 board
        self.current_winner = None # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        #samma sak som for loopen nedan
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):
            # [x|x|o] -----> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == '':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter) then return true. if invalid return false
        # här är jag.. 48:47
        pass


def play(game, x_palyer, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter

    # iterate while the game still has empty squares
    # dont have to worry about a winner, we return winner when loop brakes

    while game.empty_squares():
        # get the move form the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_palyer.get_move(game)