from asyncio.proactor_events import _ProactorSocketTransport
import random

# create a board object tp represent the minesweeper game
# create a new board object
# "dig here", or "render this game for this object"

class Board:
    def __init__(self, dim_size, num_bombs):
        # keep track of parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # Create board
        # helper function
        self.board = self.make_new_board() # plants bombs
        self.assign_values_to_board()



        # Initialize a set() to keep track of which locations we've uncoverd
        # save (row,col) tuples into this set
        self.dug = set() # if we dig at 0,0 then self.dug = {(0,0)}

    def assign_value_to_board(self):
        # bombs ar planted, now assign number 0-8 for all empty spaces which
        # represent how many neighboring bombs there are. we can precpompute these and save some
        # effort checking what's around the board later..

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this already a bomb, we dont want to calculate anythin
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)
    
    def get_num_neighboring_bombs(self, row, col):
          # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure to not go out of bounds!
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        
        return num_neighboring_bombs

    def make_new_board(self):
        # construct a new board, dim size and bombs
        # construct list of lists, 2-D board list of lists is most natural

        # genreate a board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # array (board) looks like this
        # [[None, None, ....., None,],
        # [None, None, ...., None,],
        # [None, None, ...., None,],
        # [None, None, ...., None,],
        # [None, None, ...., None,]]

        # plant bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # return random integer N such that a <= N <=b
            row = loc // self.dim_size # the number of times dim_size goes into loc to tell us
            col = loc % self.dim_size # remainder to tell us what insex in that row to loop

            if board[row][col] == '*':
                # already taken, planted bomb
                continue
            
            board[row][col] = '*' # plant bomb
            bombs_planted += 1

        return board

    def dig(self, row, col):
        # dig at location
        # return True if sucessful dig, False if bomb dug

        # scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors

        self.dug.add((row, col)) # keep track where we dig 

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue # don't dig where we already dug
                self.dig(r,c)

        # if our initial dig didn't hit a bomb, we *shouldnt't* hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object.
        # it'll print out what this function returns!
        # return a stirng that shows the board to the player

        # create a array that represent what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
         # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep



#play the game
def play(dim_size=10, num_bombs=10):
    # step 1 - Create the board and plant bombs
    board = Board(dim_size, num_bombs)

    # step 2 - show the user the board and ask for where they want to dig
    # step 3a - if location is a bomb, show "game over" message
    # step 3b - if location is not a bomb, dig recursively intil each square is at leas next to a bomb 
    # step 4 - repeat steps 2 and 3a/b until there are no more places to dig -> victory
    
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))