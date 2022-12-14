import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

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
        val = None # because the player hasn't put a value yet
        while not valid_square:
            square = input(self.letter + '\'s Turn. Input move (0-8):')
            # we're gonna check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid 
            # if that spot is not availbale on the board, we also its invalid

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these two passes successfully

            except ValueError:
                print('Invalid square. Try again')


        return val
                



    
