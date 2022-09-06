import math
import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass
 
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for out next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_squeare = False
        val = None
        while not valid_squeare:
            square = input(self.letter + '\'s turn. Input move 0-8:')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError

                valid_squeare = True
            except ValueError:
                print('Invalid square. Try again.')

        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) 
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # random choose one
        else:
            # get the square based off the minmax algorithm
            square = self.minimax(game, self.letter)['position']
        return square  

    def minimax(self, state, player):
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X' # the other player 

        #check if the previous move is a winner
        # this is our base case
        # should return position AND score, need to keep track of the score for minmax to work
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximize 
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minmax to simulate a game after makin that move
            sim_score = self.minimax(state, other_player) # now we alternate players

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # this represnts the move optimal next move 
            
            # step 4: update the dictinaries if necessary'
            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best