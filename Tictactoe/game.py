import math
import time


from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

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
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter) then return true. if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhare.. we have to check all of these!
        #check row:
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) *3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column:
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagnoals:
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diag
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diag
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all fail..
        return False


def play(game, x_palyer, o_player, print_game=True):
    #retrun the winner of the game, or None for a tie
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

        # make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X' #switch player

    if print_game:
        print('It\'s a tie...')

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0

    for _ in range(20):
        #x_player = HumanPlayer('X')
        #o_player = RandomComputerPlayer('O')
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        #o_player = HumanPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins +=11
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
        print(_)

    print(f'After 20 iterations, X: {x_wins}, O: {o_wins}, Ties: {ties}')