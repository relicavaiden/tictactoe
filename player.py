import math
import random

class Player:
    def __init__(self, letter):
        # X or O
        self.letter = letter

    # allow player their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # need to see if the correct value has been given
            # it will be taken as an integer and if not it will be invalid
            # if the spot has bee take it will be counted as invalid
            try:
                val = int(square) # input has been casted as an integer
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if the choice is wrong we catch the error
            except ValueError:
                print('Invalid square. Try again.')

        return val

class HardModeComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly choose one
        else:
            # get square based off minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter # Player
        other_player = 'O' if player == 'X' else 'X' # other player

        # first, we want to check if the previous move is winner
        # this is the base case
        if state.current_winner == other_player:
            # we need to return the position AND score
            # for minimax to work
            return {'position': None,
                    'score': 1 * (state.num_empty_squares()) + 1 if other_player == max_player else -1 *( state.num_empty_squares() + 1)
            }

        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should be larger
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate game after that move
            sim_score = self.minimax(state, other_player) # now, we alternate players
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # otherwise this will cause an issue with the recursion
            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
                else:
                    if sim_score['score'] < best['score']:
                        best = sim_score # replace best
                    
        return best