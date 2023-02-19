import time
from player import HumanPlayer, RandomComputerPlayer, HardModeComputer

class janKenPon:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # for a 3x3 board
        self.current_winner = None # is there a winner?

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # tells us what number responds to which box
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
        # could also return len(self.available_moves())

    def make_move(self, square, letter):
        # check if move is valid and assign to spot
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if there are 3 in a row anywhere..
        # first the row
        row_ind = square // 3 # how many times does 3 goes into the square
        row = self.board[row_ind * 3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only check if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all of the failed
        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (letter of the winner)! or nothing for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # while the game has not been won and there are more moves

    while game.empty_squares():
        # get move from the current player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # the function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # an empty line

            if game.current_winner:
                if print_game:
                    print(letter +  ' wins!')
                return letter


            # after the move the player switches positions
            letter = 'O' if letter == 'X' else 'X' # switches player 

        # tiny break
        time.sleep(0.8) 

        #to allow optional self play
        # if print_game:
        #     time.sleep(0.8)

            # also switches player but it is verbose
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

    if print_game:
        print('it\s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = HardModeComputer('0')
    # can play against the regular mode player
    # o_player = RandomComputerPlayer('0')
    t = janKenPon()
    play(t, x_player, o_player, print_game=True)


# for auto play mode
# if __name__ == '__main__':
#     x_wins = 0
#     o_wins = 0
#     ties = 0
#     for i in range(1000):
#         o_player = HardModeComputer('0')
#         x_player = RandomComputerPlayer('X')
#         t = janKenPon()
#         result = play(t, x_player, o_player, print_game=False) # will not print to save memory
#         if result == 'X':
#             x_wins += 1
#         elif result == 'O':
#             o_wins += 1
#         else:
#             ties += 1

#     print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties')
        